#!/usr/bin/env python3
"""¿Cuál es la cinta de mi equipo? — ARCHIVO 2031.

    python3 scripts/micinta.py

Deduce la cinta que le toca a este repositorio a partir de su nombre en
GitHub, la deja anotada en el `<meta name="equipo">` de index.html y dice qué
archivo montar. No hay nada que pedirle a nadie: cada repositorio tiene la
suya y siempre le sale la misma.

Si el meta ya está declarado, no lo toca y solo lo confirma.
"""

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
INDEX = RAIZ / "index.html"

VERDE, ROJO, GRIS, RESET = "\033[32m", "\033[31m", "\033[90m", "\033[0m"
if not sys.stdout.isatty():
    VERDE = ROJO = GRIS = RESET = ""


def slug_del_remoto() -> str:
    try:
        r = subprocess.run(
            ["git", "-C", str(RAIZ), "remote", "get-url", "origin"],
            capture_output=True, text=True,
        )
    except OSError:
        return ""
    m = re.search(r"github\.com[:/]+([^/]+/[^/.]+)", r.stdout.strip())
    return m.group(1).lower() if m else ""


def letra_de(slug: str, letras: list[str]) -> str:
    digest = hashlib.sha256(slug.encode("utf-8")).hexdigest()
    return letras[int(digest, 16) % len(letras)]


def main() -> int:
    claves = RAIZ / "scripts" / "claves.json"
    if not claves.exists():
        sys.exit("✗ falta scripts/claves.json")
    letras = sorted(json.loads(claves.read_text(encoding="utf-8"))["equipos"])

    html = INDEX.read_text(encoding="utf-8")
    m = re.search(r'<meta name="equipo" content="([^"]*)"', html)
    declarada = (m.group(1).strip().upper() if m else "")

    if declarada in letras:
        print(f"\n  Su equipo ya está declarado: {VERDE}{declarada}{RESET}")
        print(f"  Cinta: {VERDE}incidente/equipo-{declarada}.bundle{RESET}\n")
        return 0

    slug = slug_del_remoto()
    if not slug:
        sys.exit(
            "✗ este repositorio no tiene un remoto de GitHub configurado.\n"
            "  Corran este script dentro del clon de SU repositorio, no de la plantilla."
        )

    letra = letra_de(slug, letras)
    INDEX.write_text(
        html.replace(
            f'<meta name="equipo" content="{declarada}" />',
            f'<meta name="equipo" content="{letra}" />',
        ),
        encoding="utf-8",
    )

    print(f"\n  Repositorio: {slug}")
    print(f"  Su equipo es: {VERDE}{letra}{RESET}")
    print(f"  Cinta:        {VERDE}incidente/equipo-{letra}.bundle{RESET}")
    print(f"\n  {GRIS}Anotado en el <meta name=\"equipo\"> de index.html.{RESET}")
    print(f"  {GRIS}Commiteen ese cambio: es lo que decide contra qué se les corrige.{RESET}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
