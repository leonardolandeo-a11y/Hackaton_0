# La cinta del incidente

En esta carpeta hay un archivo por equipo:

```text
incidente/equipo-A.bundle
incidente/equipo-B.bundle
...
```

**Solo uno es el suyo.** El equipo docente les dice cuál, y esa misma letra va
en el `<meta name="equipo">` de `index.html`. Los demás contienen datos
distintos: copiarle a otro equipo garantiza fallar la corrección.

## Qué es esto

Un **git bundle** es un repositorio entero comprimido en un solo archivo:
commits, ramas, etiquetas y todo lo demás. Se usa de verdad para mover historia
entre máquinas que no se pueden conectar: un disco que se lleva en la mano, un
servidor sin red, un respaldo en cinta.

Para ustedes significa una cosa muy concreta: **su repositorio arranca vacío y
la historia del incidente llega aparte.** El historial de su repositorio lo
construyen ustedes desde el commit uno. La historia que van a investigar vive
dentro de este archivo y no la escribió nadie del equipo.

## Cómo se trabaja con él

Git trata un bundle como si fuera un remoto: pueden preguntarle qué contiene
antes de tocarlo, y pueden traérselo con un `fetch` normal indicando a dónde
quieren que aterrice cada referencia.

```bash
git bundle --help
```

Léanlo. Son dos pantallas y contesta las tres preguntas que van a tener.

Una vez traído, esos commits son objetos normales de su repositorio, y se les
puede aplicar cualquier operación de Git **aunque no compartan ningún ancestro**
con su rama. Esa es exactamente la operación que van a necesitar.

> ⚠️ Cuidado con dónde lo dejan caer. Varias herramientas de Git buscan cierto
> tipo de referencias **siempre en una ubicación fija**, no donde ustedes las
> hayan puesto. Si un comando les dice que no hay nada, no den por hecho que no
> hay nada.

No modifiquen ni borren los `.bundle`: el corrector los usa.
