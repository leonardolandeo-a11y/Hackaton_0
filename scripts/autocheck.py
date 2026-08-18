#!/usr/bin/env python3
"""Autocomprobación del equipo — ARCHIVO 2031.

    python3 scripts/autocheck.py

Dice qué falta SIN decir las respuestas. El sello se valida por hash: si las
seis palabras son correctas verás ✓, y si no, no hay pistas.

Revisa el repositorio local y, si tienen la CLI `gh` autenticada, también el
estado en GitHub (PRs, revisiones y Pages). Si `gh` no está, lo dice claramente
en vez de dar por bueno lo que no comprobó.

Es un subconjunto de la corrección oficial: pasarla es necesario, no
suficiente. La letra del equipo se lee del `<meta name="equipo">` de
index.html.
"""

import hashlib
import json
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FRAGMENTOS_SELLO = 2

VERDE, ROJO, GRIS, RESET = "\033[32m", "\033[31m", "\033[90m", "\033[0m"
if not sys.stdout.isatty():
    VERDE = ROJO = GRIS = RESET = ""

resultados: list[tuple[bool, str, str]] = []


def check(ok: bool, titulo: str, ayuda: str = "") -> None:
    resultados.append((bool(ok), titulo, ayuda))


def normalizar_sello(texto: str) -> str:
    """`PALABRA - PALABRA` y `palabra-palabra` valen igual."""
    return re.sub(r"\s*-\s*", "-", texto.strip().upper().lstrip("\ufeff"))


def leer(rel: str) -> str:
    p = RAIZ / rel
    return p.read_text(encoding="utf-8-sig", errors="replace") if p.exists() else ""


def git(*args: str) -> str:
    try:
        r = subprocess.run(["git", "-C", str(RAIZ), *args], capture_output=True, text=True)
    except OSError:
        return ""
    return r.stdout.strip() if r.returncode == 0 else ""


html = leer("index.html")
m_equipo = re.search(r'<meta name="equipo" content="([^"]*)"', html)
equipo = (m_equipo.group(1).strip().upper() if m_equipo else "")

claves_path = RAIZ / "scripts" / "claves.json"
if not claves_path.exists():
    sys.exit("✗ falta scripts/claves.json")
CLAVES = json.loads(claves_path.read_text(encoding="utf-8"))

if equipo not in CLAVES["equipos"]:
    sys.exit(
        f'✗ equipo "{equipo}" desconocido.\n'
        f'  Declaren su letra en el <meta name="equipo" content="?"> de index.html.\n'
        f"  Válidas: {', '.join(CLAVES['equipos'])}"
    )
SELLO_SHA256 = CLAVES["equipos"][equipo]
TAG_ENTREGA = CLAVES["tag_entrega"]

# --- 1. La cinta está montada -------------------------------------------------
refs_locales = git("for-each-ref", "--format=%(refname)").splitlines()
check(
    len(refs_locales) > 2,
    "la cinta del incidente está montada en el repositorio",
)

# --- 2. Auditoría estructural -------------------------------------------------
auditoria = subprocess.run(
    [sys.executable, str(RAIZ / "scripts" / "audit.py")], capture_output=True, text=True
)
ultima = auditoria.stdout.strip().splitlines()
check(auditoria.returncode == 0, "scripts/audit.py pasa", ultima[-1] if ultima else "")

# --- 3. Archivos recuperados --------------------------------------------------
for i in range(1, FRAGMENTOS_SELLO + 1):
    rel = f"bitacora/frag-{i:02d}.txt"
    check((RAIZ / rel).exists(), f"{rel} presente")

check((RAIZ / "assets" / "sello.svg").exists(), "assets/sello.svg recuperado")

check((RAIZ / "bitacora" / "SELLO.txt").exists(), "bitacora/SELLO.txt existe")
check((RAIZ / "bitacora" / "INFORME.md").exists(), "bitacora/INFORME.md existe")

# --- 4. index.html ------------------------------------------------------------
relleno = ("NOMBRE PENDIENTE", "ROL PENDIENTE", "usuario-github-", "Fotografía pendiente")
check(
    not any(marca in html for marca in relleno),
    "las 3 tarjetas ya no tienen datos de relleno",
)

ranuras = re.findall(
    r'data-frag="(\d{2})".*?<code class="frag__palabra">([^<]*)</code>', html, flags=re.DOTALL
)
llenas = [(n, w.strip().upper()) for n, w in ranuras if w.strip() and w.strip() != "???"]
check(
    len(llenas) == FRAGMENTOS_SELLO,
    f"las {FRAGMENTOS_SELLO} ranuras de index.html están llenas",
    f"llenas: {len(llenas)}/{FRAGMENTOS_SELLO}",
)

# --- 5. Sello -----------------------------------------------------------------
m_sello = re.search(r"^\s*SELLO\s*:\s*(.+)$", leer("bitacora/SELLO.txt"),
                    flags=re.MULTILINE | re.IGNORECASE)
sello = normalizar_sello(m_sello.group(1)) if m_sello else ""
sello_ok = bool(sello) and hashlib.sha256(sello.encode()).hexdigest() == SELLO_SHA256
check(sello_ok, "el sello es CORRECTO", "hash no coincide" if sello else "falta la línea SELLO:")

m_html = re.search(r'id="sello-valor"[^>]*>([^<]*)<', html)
check(
    sello_ok and bool(m_html) and normalizar_sello(m_html.group(1)) == sello,
    "index.html muestra el sello correcto",
)

orden = [w for _, w in sorted(llenas, key=lambda t: t[0])]
check(
    len(llenas) == FRAGMENTOS_SELLO and sello_ok and "-".join(orden) == sello,
    "las ranuras coinciden con SELLO.txt",
)

# --- 6. Informe ---------------------------------------------------------------
informe = leer("bitacora/INFORME.md")
citados = len(set(re.findall(r"FRAG-0[1-6]", informe.upper())))
comandos = len(re.findall(r"git\s+[a-z-]+", informe))
check(
    citados >= FRAGMENTOS_SELLO and comandos >= CLAVES["min_comandos_informe"],
    "INFORME.md documenta cada hallazgo con su comando",
    f"fragmentos citados: {citados}/{FRAGMENTOS_SELLO}, "
    f"comandos: {comandos}/{CLAVES['min_comandos_informe']}",
)

# --- 7. Entrega ---------------------------------------------------------------
tag = TAG_ENTREGA
check(
    git("cat-file", "-t", f"refs/tags/{tag}") == "tag",
    f"existe la etiqueta ANOTADA {tag}",
    "una etiqueta ligera no cuenta",
)


# --- 8. GitHub ----------------------------------------------------------------
MIN_PR = CLAVES["min_prs"]
omitido_github = ""


def gh(ruta: str):
    r = subprocess.run(["gh", "api", "--paginate", ruta], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or "gh falló").strip().splitlines()[0])
    crudo = r.stdout.strip()
    return json.loads(re.sub(r"\]\s*\[", ",", crudo)) if crudo else []


m_slug = re.search(r"github\.com[:/]+([^/]+/[^/.]+)", git("remote", "get-url", "origin"))
if not m_slug:
    omitido_github = "Este repositorio no tiene un remoto de GitHub configurado."
elif not shutil.which("gh"):
    omitido_github = "No tienen instalada la CLI de GitHub (gh)."
else:
    slug = m_slug.group(1)
    try:
        pulls = gh(f"repos/{slug}/pulls?state=all&per_page=100")
        mergeados = [p for p in pulls if p.get("merged_at")]
        check(
            len(mergeados) >= MIN_PR,
            f"al menos {MIN_PR} Pull Requests mergeados",
            f"mergeados: {len(mergeados)}/{MIN_PR}",
        )

        con_revision = 0
        for pr in mergeados:
            autor = (pr.get("user") or {}).get("login", "").lower()
            revisiones = gh(f"repos/{slug}/pulls/{pr['number']}/reviews")
            if any(
                rv.get("state") == "APPROVED"
                and (rv.get("user") or {}).get("login", "").lower() != autor
                for rv in revisiones
            ):
                con_revision += 1
        check(
            bool(mergeados) and con_revision == len(mergeados),
            "cada PR mergeado tiene aprobación de otro integrante",
            f"con revisión cruzada: {con_revision}/{len(mergeados)}",
        )

        url, pista = "", ""
        try:
            pages = gh(f"repos/{slug}/pages")
            if isinstance(pages, dict):
                url = pages.get("html_url", "")
        except RuntimeError:
            pista = "Pages no está activado: Settings → Pages → Source: GitHub Actions"
        vivo = False
        if url:
            try:
                with urllib.request.urlopen(url, timeout=15) as resp:
                    vivo = resp.status == 200
                pista = url
            except urllib.error.HTTPError as exc:
                pista = (f"{url} devuelve {exc.code}: si acaban de desplegar, "
                         "el primer build tarda un par de minutos")
            except (urllib.error.URLError, TimeoutError, OSError):
                pista = f"{url} no responde todavía"
        elif not pista:
            pista = "Pages activado pero aún sin URL: esperen al primer despliegue"
        check(vivo, "GitHub Pages publicado y respondiendo", pista)
    except RuntimeError as exc:
        omitido_github = f"La CLI de GitHub no pudo consultar {slug}: {exc}"

# --- Reporte ------------------------------------------------------------------
print(f"\n  ARCHIVO 2031 · autocomprobación — equipo {equipo}")
print("  " + "─" * 56)
for ok, titulo, ayuda in resultados:
    marca = f"{VERDE}✓{RESET}" if ok else f"{ROJO}✗{RESET}"
    extra = f"  {GRIS}{ayuda}{RESET}" if ayuda and not ok else ""
    print(f"  {marca} {titulo}{extra}")

logrados = sum(1 for ok, _, _ in resultados if ok)
completo = logrados == len(resultados)
print("  " + "─" * 56)
print(f"  {logrados}/{len(resultados)} comprobaciones superadas")

if omitido_github:
    print()
    print(f"  {ROJO}⚠ No puedo evaluarlos por completo.{RESET}")
    print(f"    {omitido_github}")
    print(f"    {GRIS}Sin la CLI de GitHub no puedo comprobar tres cosas que SÍ puntúan:{RESET}")
    print(f"    {GRIS}PRs mergeados, revisión cruzada y GitHub Pages.{RESET}")
    print(f"    {GRIS}Instálenla en https://cli.github.com y hagan `gh auth login`.{RESET}")
    completo = False

print()
print(f"  {VERDE}LISTO PARA ENTREGAR{RESET}\n" if completo else f"  {ROJO}TODAVÍA NO{RESET}\n")
sys.exit(0 if completo else 1)
