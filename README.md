# 🚀 Hackatón 0 – CS2031

¡Bienvenidos! 🎉
Desde el curso **CS2031** les damos una cordial bienvenida al ciclo **2026-2**. El foco sigue siendo el mismo que siempre: colaboración bajo presión, conflictos de Git y trabajo en equipo real.

## 🤔 ¿Qué trae esta Hackatón?

Esta **Hackatón 0** es una primera muestra del concepto de hackatones. Los equipos son de **exactamente 3 integrantes**, tienen **1 hora** y el repositorio que heredan está roto a propósito. El foco:

> **Git + GitHub + trabajo en equipo**

No hace falta saber programar backend. Ni siquiera hace falta escribir mucho HTML. El reto está en **usar Git de verdad, coordinarse y dejar un historial que se sostenga solo**.

Si aún no viste el video de introducción a Git y GitHub, **este es el momento**: [👉 Video de introducción a Git y GitHub](https://www.youtube.com/watch?v=8CmZysIzcbc)

Casi todo lo que necesitan ya lo vieron ahí: clonar, ramas, commits, push, Pull Requests y conflictos. Lo que falta lo van a aprender hoy, buscando.

**Todo lo que pide este enunciado es obligatorio.** No hay bonus ni tareas opcionales: si está aquí, cuenta para la nota.

### ⚠️ Sobre usar IA

Van a usarla igual, así que hablemos claro: **está permitida**. Úsenla para aprender comandos, que para eso es buenísima.

Lo que no les va a resolver son dos cosas:

1. **La información que necesitan no existe fuera de este repositorio.** No está en internet y no se deduce razonando. Está guardada dentro de un archivo que van a tener que aprender a abrir con Git.
2. **La entrega no es un archivo: es un historial.** Se corrige la forma del grafo de commits que ustedes construyan — que haya merges de verdad y un conflicto resuelto entre los tres. Eso no se pega desde un chat: se hace.

> 🎯 **Regla de oro:** cada hallazgo se documenta con el comando exacto que lo produjo. Si no pueden reproducirlo delante de un TA, no cuenta.

---

## 👥 Trabajo en equipo

Los equipos son de **3 integrantes fijos**. Repártanse estos roles al empezar:

| Rol | Responsabilidad |
|---|---|
| 🧭 **Líder** | Crea el repositorio y los issues, revisa y mergea los PR, conduce la resolución del conflicto. |
| 🔎 **Arqueólogo** | Busca los dos fragmentos perdidos en la historia. |
| 🧰 **Integrador de la web** | Completa la página, deja la auditoría en verde y el despliegue vivo. |

Los roles no son excusas: **los tres deben tener commits, PRs y revisiones**. La corrección lo verifica commit por commit.

---

## ⏱️ Plan de la hora

En 60 minutos no hay margen para improvisar el orden. Este reparto está medido:

| Tiempo | Qué |
|---|---|
| 0:00 – 0:12 | Issue **#1** — Crear el repo, configurarlo y montar la cinta |
| 0:12 – 0:30 | Issue **#2** — Los dos fragmentos y el glifo |
| 0:30 – 0:48 | Issue **#3** — Datos personales y el conflicto |
| 0:48 – 1:00 | Issue **#4** — Sello, informe, etiqueta y despliegue |

> ⚡ **Hagan esto antes de que arranque el cronómetro:** que el líder cree el repositorio e invite a los otros dos, y que **ellos acepten la invitación**. Si la aceptan a mitad de sesión, pierden diez minutos sin poder abrir un solo PR.

Si a los 30 minutos les falta un fragmento, **salten al issue #3 igual**: las tarjetas y el despliegue valen más que el fragmento que falta, y el conflicto necesita a los tres a la vez.

---

## 📜 El reto

Un TA (que no diremos quién 🤫) volvió a meter mano en el repositorio, pero esta vez se le fue la mano de verdad. Ejecutó un script de "limpieza" sobre el **ARCHIVO 2031**, una terminal web con la bitácora del proyecto, y lo que ustedes heredan es el escombro:

- La bitácora está vacía: sus **fragmentos** desaparecieron del árbol de trabajo.
- El glifo del sello no está por ningún lado.
- Las tarjetas del equipo siguen con datos de relleno.

Pero del repositorio original quedó **una cinta de respaldo**: el archivo `incidente/equipo-<X>.bundle`. Ahí adentro está toda la historia previa al incidente.

🎯 **Tu objetivo:** montar la cinta, recuperar los **dos fragmentos** del sello y el glifo, completar el equipo y desplegar la página en **GitHub Pages**.

Cuando las dos palabras estén en su sitio, la terminal se sella sola y su estado pasa de `INCOMPLETO` a `RESTAURADO`.

---

## 👑 Organización del equipo

- Elijan un **líder** que cree el repositorio con **`Use this template` → `Create a new repository`**. Nombre sugerido: `archivo-2031-<equipo>`.
  > ⚠️ **Márquenlo Public.** GitHub Pages solo funciona en repositorios privados con planes de pago, y sus cuentas son gratuitas: si lo dejan privado, no van a poder desplegar.
  >
  > Van a recibir un repositorio con **un solo commit**: el suyo. Eso es correcto y es el punto — **su historial empieza en cero y lo construyen ustedes.** La historia que van a investigar viaja aparte, en la cinta.
- El líder da acceso de colaborador a los otros 2 integrantes, y ellos **aceptan la invitación**.
- En `Settings → Pages → Source`: seleccionen **GitHub Actions**. Sin esto no hay despliegue.
- En `Settings → General → Pull Requests`: **desactiven "Allow squash merging"**. El squash aplasta el trabajo de sus compañeros y la corrección lo penaliza.
- Cada integrante trabaja en **su propia rama** y abre un **PR** para que otro lo revise y acepte. **Nadie se auto-aprueba.**
- Esperamos **al menos 3 PR mergeados**. El conflicto se resuelve en equipo, **no individualmente**.

Y lo primero de todo, ya dentro de su clon: **averigüen cuál es su cinta**.

```bash
python3 scripts/micinta.py
```

Ese comando mira el nombre de **su** repositorio, deduce qué cinta le toca y lo anota en el `<meta name="equipo">` de `index.html`. Commiteen ese cambio: es lo que decide contra qué se les corrige.

No hay nada que pedirle a nadie ni que esperar. Cada repositorio tiene su propia cinta con palabras distintas, siempre la misma, y se deduce sola. Cambiarla a mano para usar la de otro equipo se detecta y anula la entrega.

---

## ✅ Checklist del equipo (issues a crear por el líder)

### #1 — Montar la cinta

Lean `incidente/LEEME.md`. Un **git bundle** es un repositorio entero dentro de un solo archivo: commits, ramas, etiquetas y todo lo demás. Git lo trata como si fuera un remoto, así que se le puede hacer `fetch`.

Empiecen mirando qué trae, antes de tocarlo:

```bash
git bundle verify incidente/equipo-<X>.bundle
git bundle list-heads incidente/equipo-<X>.bundle
```

Antes de seguir, respondan estas dos en el issue:

1. ¿Cuántas referencias trae la cinta, y cuántas de ellas **no** son ramas?
2. Una vez montada, ¿cuántos commits tiene su rama principal y quién los firmó?

---

### #2 — Los dos fragmentos (uno para cada uno)

Están escondidos con técnicas **distintas**. Esa es toda la gracia: el comando que sirve para uno no sirve para el otro.

| # | Pista (es lo único que van a recibir) |
|---|---|
| **FRAG-01** | Un archivo que estuvo en la rama principal de la cinta y al final ya no está. Los archivos borrados siguen vivos en el commit **anterior** al que los borró. |
| **FRAG-02** | Un respaldo hecho *antes* del incidente. Está anclado a una referencia que **no es una rama**, y el texto no está dentro de ningún archivo: está en la referencia misma. |

Cada fragmento es un bloque de texto con este aspecto:

```text
======================================
   ARCHIVO 2031 - FRAGMENTO 0X/02
======================================
origen : ...
palabra: ...
codigo : ...
--------------------------------------
Transcribir tal cual. Se compara linea a linea.
```

**Entregable:** los dos bloques completos, transcritos **sin modificar**, en `bitacora/frag-01.txt` y `bitacora/frag-02.txt`.

> 💡 Redirigir la salida de un comando a un archivo (`>`) es más fiable —y más honesto— que copiar y pegar del terminal. El `codigo` es aleatorio: no se adivina y no se deduce.

Y de paso: **el glifo del sello** (`assets/sello.svg`) también se perdió, y está guardado en el mismo sitio que FRAG-02. Recupérenlo íntegro; la página lo necesita.

---

### #3 — Datos personales (1 PR por persona)

Cada integrante, **en su propia rama** `feat/member-<nombre>`, hace dos cosas en `index.html`:

1. Completa **su** tarjeta: foto (`src` y `alt` del `<img>`), nombre (`<h3 class="tarjeta__nombre">`), rol (`<p class="tarjeta__rol">`), usuario y los `href` de GitHub y LinkedIn.
2. Añade su nombre a la línea del **turno de guardia**, dentro de `<span class="equipo__nombres">`.

**Conflicto esperado:** los tres escriben en **esa misma línea** y salen de la misma base → el segundo y el tercer PR van a chocar sí o sí. Deberán resolverlo conservando los tres nombres.

Ejemplo de tarjeta correctamente completada:

```html
<article class="tarjeta">
  <img
    class="tarjeta__foto"
    src="https://avatars.githubusercontent.com/u/0000000"
    alt="Foto de Sparky García"
  />
  <h3 class="tarjeta__nombre">Sparky García</h3>
  <p class="tarjeta__rol">Backend Developer</p>
  <p class="tarjeta__usuario">@sparkygarcia</p>
  <ul class="tarjeta__enlaces">
    <li><a class="tarjeta__enlace" href="https://github.com/sparkygarcia">GitHub</a></li>
    <li><a class="tarjeta__enlace" href="https://www.linkedin.com/in/sparkygarcia">LinkedIn</a></li>
  </ul>
</article>
```

---

### #4 — Sello, informe y entrega (1 PR)

1. Escriban las dos palabras en las dos ranuras de `index.html`.
2. Escriban el sello completo en `#sello-valor`. La página se verifica sola: si es correcto, el estado pasa a **RESTAURADO**.
3. `python3 scripts/audit.py` debe pasar en `main`.
4. Etiqueten la entrega con una **etiqueta anotada** (no ligera) cuyo mensaje contenga el sello:

   ```bash
   git tag -a v1.0.0 -m "Archivo restaurado. Sello: PALABRA-PALABRA"
   git push origin v1.0.0
   ```

**Archivos que deben quedar en `main`:**

| Ruta | Contenido |
|---|---|
| `bitacora/frag-01.txt`, `frag-02.txt` | Los dos fragmentos transcritos sin alterar. |
| `bitacora/SELLO.txt` | Formato exacto, ver abajo. |
| `bitacora/INFORME.md` | La tabla de la investigación, ver abajo. |
| `index.html` | Letra del equipo, ranuras, sello, 3 tarjetas y turno de guardia. |
| `assets/sello.svg` | Recuperado, íntegro. |
| `README.md` | Con la URL de GitHub Pages del equipo. |

`bitacora/SELLO.txt`:

```text
FRAG-01: PALABRA
FRAG-02: PALABRA
SELLO: PALABRA-PALABRA
```

`bitacora/INFORME.md`: una tabla de tres filas, sin prosa. Una por fragmento y una por el glifo.

```markdown
| Hallazgo | Dónde estaba | Técnica de Git | Comando exacto | Referencia |
|---|---|---|---|---|
| FRAG-01 | ... | ... | `git ...` | `a1b2c3d` |
```

---

### ✅ Publicado en GitHub Pages

El deploy es **automático** gracias al workflow `.github/workflows/pages.yml`: cada push a `main` publica la página. Pero **hay que activarlo una vez**, y es el paso que más se olvida:

**`Settings` → `Pages` → en *Source*, elegir `GitHub Actions`.** Háganlo al principio, junto con lo demás de la Fase 0.

Hasta que lo hagan, el workflow de despliegue **no falla**: se queda quieto y les deja un aviso amarillo diciendo justo eso. Nada de X rojas por algo que todavía no tenían por qué haber hecho.

La URL aparece en **Settings → Pages** y en la pestaña **Environments → github-pages**. Cópienla al `README.md`.

> ⚠️ **Las cuatro cosas que hacen fallar Pages**, por orden de frecuencia:
>
> 1. **No activaron Pages** con *Source: GitHub Actions*. Es lo de arriba.
> 2. **El repositorio es privado.** Pages en repos privados requiere plan de pago y sus cuentas son gratuitas. Tiene que ser **Public**.
> 3. **La auditoría falla.** `pages.yml` corre `scripts/audit.py` antes de desplegar y **se niega a publicar un sitio roto**. Si rompieron un enlace o borraron un `alt`, no hay deploy. Arréglenlo y vuelvan a pushear.
> 4. **Acaban de desplegar.** El primer build tarda **uno o dos minutos** y hasta que termina la URL devuelve 404. No es un error: esperen y recarguen.
>
> Si `autocheck` les dice que Pages no responde, léanlo: distingue estos casos.

---

## ⚡ Ejemplo de conflicto en `index.html`

Cuando los tres editan la línea del turno de guardia, Git genera algo así:

```html
<<<<<<< HEAD
<p class="equipo__lista">Turno de guardia: <span class="equipo__nombres">Ana Torres</span></p>
=======
<p class="equipo__lista">Turno de guardia: <span class="equipo__nombres">Luis Ríos</span></p>
>>>>>>> feat/member-luisrios
```

La tarea del equipo es **resolverlo manualmente**, eliminando los marcadores y preservando los datos de ambos:

```html
<p class="equipo__lista">Turno de guardia: <span class="equipo__nombres">Ana Torres, Luis Ríos</span></p>
```

No vale `--ours`, no vale `--theirs`, y no vale borrar el nombre del otro para volver a escribirlo después.

---

## 🗂️ Resumen de ramas y PRs

| Rama | Responsable | Tipo | PR |
|---|---|---|---|
| `feat/member-<nombre>` | Cada integrante | Datos personales | 1 por persona |
| `arqueo/fragmentos` | Arqueólogo | Los dos fragmentos y el glifo | 1 PR |
| `feat/sello` | Líder | Sello, informe y entrega | 1 PR |

> Los nombres son sugerencias, salvo `feat/member-<nombre>`, que sí se revisa. Lo que **no** es negociable: todo entra por Pull Request, y esperamos **al menos 3 PR mergeados**.

## ⚙️ GitHub Actions incluidas

| Workflow | Archivo | Se ejecuta en |
|---|---|---|
| Auditoría del sitio | `.github/workflows/audit.yml` | Cada PR hacia `main` y cada push |
| Deploy a GitHub Pages | `.github/workflows/pages.yml` | Cada push a `main` |

**`audit.yml`** revisa que no queden marcadores de conflicto sin resolver y corre `scripts/audit.py`: enlaces internos que apunten a un `id` real, sin scripts no autorizados, imágenes con `alt`, y el bloque de accesibilidad del CSS en su sitio.

**`pages.yml`** despliega tras cada merge a `main`, y **se niega a desplegar si la auditoría falla**.

---

## 🧪 Los tests: cómo saber si ya terminaron

No adivinen. Pregúntenle al repositorio. Hay dos scripts y se corren desde la raíz del proyecto:

```bash
python3 scripts/audit.py       # ¿está sano el sitio?
python3 scripts/autocheck.py   # ¿está completa la entrega?
```

**`scripts/audit.py`** es el detector: enlaces internos, scripts no autorizados, `alt` en las imágenes y el bloque de accesibilidad del CSS. Devuelve `0` si está sano y `1` si está roto. Es el mismo que corre en cada PR y el que decide si la página se despliega.

**`scripts/autocheck.py`** es la autocomprobación de la entrega: fragmentos, sello, tarjetas, turno de guardia, informe y etiqueta. Si además tienen la [CLI de GitHub](https://cli.github.com) autenticada (`gh auth login`), revisa también sus PRs mergeados, las revisiones cruzadas y si Pages está vivo. Termina con un veredicto:

```
  17/17 comprobaciones superadas

  LISTO PARA ENTREGAR
```

Si no tienen `gh`, **corre igual todo lo demás** y les dice con claridad qué se quedó sin revisar:

```
  ⚠ No puedo evaluarlos por completo.
    No tienen instalada la CLI de GitHub (gh).
    Sin la CLI de GitHub no puedo comprobar tres cosas que SÍ puntúan:
    PRs mergeados, revisión cruzada y GitHub Pages.
```

Córranlo cada vez que mergeen algo. Es un subconjunto de la corrección oficial, así que pasarlo es **necesario pero no suficiente**: el bloque A, que es la forma de su historial, se corrige aparte.

### 🔒 Los tests no se tocan

> **Modificar cualquiera de estos archivos es nota 0 en toda la hackatón:**
>
> - `scripts/audit.py`
> - `scripts/autocheck.py`
> - `scripts/micinta.py`
> - `scripts/sello.js`
> - `scripts/claves.json`
> - `incidente/*.bundle`
>
> No es una amenaza vacía: la corrección compara esos archivos y su cinta contra
> los originales **antes** de puntuar. Si algo cambió, lo dice, lista qué
> tocaron y pone la nota en cero.

Están probados: no tienen falsos positivos, toleran finales de línea de Windows y espacios sobrantes, y no dependen de nada que ustedes tengan que instalar salvo Python 3 y Git. **Si creen que un test falla injustamente, no lo editen: llamen a un TA.** Si tienen razón, lo arreglamos nosotros y todos ganan; si lo editan, no hay nada que discutir.

Lo que sí pueden (y deben) tocar es todo lo demás: `index.html`, `styles/`, `bitacora/`, `README.md`.

---

## 🧾 Rúbrica (100 puntos)

| Bloque | Pts | Qué se mide |
|---|---|---|
| **A · Historia propia** | 25 | Historia independiente de la cinta y ≥8 commits del equipo · los 3 integrantes con ≥2 commits · ≥3 merge commits (nada de squash) · al menos un merge que integra un conflicto real · las 3 ramas `feat/member-*`. |
| **B · Los fragmentos** | 30 | FRAG-01 y FRAG-02 transcritos sin una sola alteración (12 c/u) · sello correcto (6). |
| **C · Sitio** | 20 | Auditoría en verde (5) · ranuras y sello en la página (5) · glifo recuperado (5) · 3 tarjetas y turno de guardia (5). |
| **D · Entrega** | 20 | Etiqueta anotada con el sello (6) · ≥3 PR mergeados (5) · revisión cruzada (5) · Pages vivo (4). |
| **E · Informe** | 5 | La tabla con técnica, comando y referencia por hallazgo. |

## 🚫 Descalificaciones

Son pocas y son claras:

- `git push --force` sobre `main`.
- Squash de los PR de los compañeros (aplasta su autoría).
- Escribir los fragmentos a mano sin recuperarlos. Se comparan **línea a línea**, incluido el `codigo` aleatorio.
- Auto-aprobarse los PR.
- Modificar cualquier archivo de `scripts/` o cualquier `.bundle`.
- Cambiar a mano la letra del equipo para usar la cinta de otro.

---

## 🧰 Caja de herramientas

Hay más comandos de los que necesitan y **no están en orden**. Parte del reto es elegir cuál va con cada problema.

```bash
git bundle verify | list-heads <archivo>
git fetch <archivo.bundle> '+refs/*:refs/<destino>/*'
git for-each-ref
git log --all --oneline --graph --decorate
git log --diff-filter=D -- <ruta>
git show <ref>:<ruta>
git checkout <ref> -- <ruta>
git tag -n99
git tag -a <nombre> -m '<mensaje>'
git cat-file -t | -p <objeto>
git merge-base <a> <b>
git reflog
```

---

💡 Recuerden: la página es **estática**. No hay backend, y el HTML que van a escribir cabe en una pantalla. El desafío está en **investigar, coordinarse y dejar un historial que cuente la verdad de lo que hicieron**.

Van a pasar los primeros diez minutos convencidos de que el repositorio está simplemente roto y de que no hay nada que encontrar. Es exactamente la sensación de entrar a un proyecto real que alguien más rompió antes de irse. La diferencia entre quien sabe Git y quien memorizó `add`, `commit` y `push` es saber que la información sigue ahí, y saber preguntarle al repositorio por ella.

¡Éxito equipo! 💪 Con cariño, el equipo docente de CS2031.
