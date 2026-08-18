#!/usr/bin/env python3
"""Auditoría estructural de ARCHIVO 2031.

    python3 scripts/audit.py

Códigos de salida:
    0   -> el árbol está sano
    1   -> el árbol está roto
    125 -> el árbol no es evaluable
"""

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
INDEX = RAIZ / "index.html"
BASE_CSS = RAIZ / "styles" / "base.css"

fallas: list[str] = []


def revisar_enlaces_internos(html: str) -> None:
    ids = set(re.findall(r'\bid="([^"]+)"', html))
    for destino in re.findall(r'href="#([^"]+)"', html):
        if destino not in ids:
            fallas.append(f'enlace roto: href="#{destino}" no coincide con ningún id')


def revisar_scripts_externos(html: str) -> None:
    for src in re.findall(r'<script[^>]*\bsrc="([^"]+)"', html):
        if "tracker" in src or "pixel" in src or src.startswith("http"):
            fallas.append(f"script no autorizado: {src}")


def revisar_imagenes(html: str) -> None:
    for etiqueta in re.findall(r"<img\b[^>]*>", html, flags=re.IGNORECASE):
        alt = re.search(r'\balt="([^"]*)"', etiqueta)
        if alt is None:
            fallas.append("imagen sin atributo alt")
        elif not alt.group(1).strip():
            fallas.append("imagen con atributo alt vacío")


def revisar_recursos_locales(html: str) -> None:
    """Una hoja de estilos o un script que apunta a la nada rompe la página."""
    refs = re.findall(r'<link[^>]*\brel="stylesheet"[^>]*\bhref="([^"]+)"', html)
    refs += re.findall(r'<script[^>]*\bsrc="([^"]+)"', html)
    for ref in refs:
        if ref.startswith(("http://", "https://", "//", "data:")):
            continue
        if not (RAIZ / ref).exists():
            fallas.append(f"recurso enlazado que no existe: {ref}")


def revisar_marcadores_de_conflicto(html: str) -> None:
    for marcador in ("<<<<<<<", "=======", ">>>>>>>"):
        if re.search(rf"^{re.escape(marcador)}", html, flags=re.MULTILINE):
            fallas.append(f"marcador de conflicto sin resolver: {marcador}")
            break


def revisar_accesibilidad_css(css: str) -> None:
    if "--contraste-alto" not in css or "--foco" not in css:
        fallas.append(
            "styles/base.css perdió el bloque de accesibilidad (--contraste-alto / --foco)"
        )
    if ":focus-visible" not in css:
        fallas.append("styles/base.css ya no define estilos de :focus-visible")



def main() -> int:
    if not INDEX.exists():
        print("[audit] index.html no existe todavía; commit no evaluable.")
        return 125

    html = INDEX.read_text(encoding="utf-8", errors="replace")
    revisar_enlaces_internos(html)
    revisar_scripts_externos(html)
    revisar_recursos_locales(html)
    revisar_imagenes(html)
    revisar_marcadores_de_conflicto(html)

    if BASE_CSS.exists():
        revisar_accesibilidad_css(BASE_CSS.read_text(encoding="utf-8", errors="replace"))
    else:
        fallas.append("falta styles/base.css")

    if fallas:
        print(f"[audit] {len(fallas)} problema(s) detectado(s):")
        for f in fallas:
            print(f"  ✗ {f}")
        return 1

    print("[audit] ✓ árbol de trabajo sano")
    return 0


if __name__ == "__main__":
    sys.exit(main())
