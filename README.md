# Radar de Siniestros

Seguimiento de siniestros de **Río Uruguay Seguros** en una sola página web.
Reemplaza el "me perdí en el Excel" por una vista donde se ve, de un vistazo,
qué siniestro está por vencer y hace cuánto que no lo tocás.

Es **un solo archivo** (`index.html`), sin librerías ni servidor. Se puede subir a
Vercel, abrir desde el celular o incluso abrir haciendo doble clic.

---

## Qué resuelve

| Problema | Cómo lo resuelve |
|---|---|
| Se pierde el seguimiento de los siniestros, sobre todo los de terceros | Los de terceros van marcados en violeta y con un plazo de alerta más corto que el resto |
| No se sabe hace cuánto que no se mira un siniestro | Cada tarjeta tiene un contador grande de días y un botón **Lo revisé** |
| Al importar la planilla de RUS se cargan siniestros repetidos | Antes de agregar nada, muestra cuántos **faltaban**, cuántos **ya estaban** y cuáles son |
| El Excel tiene tantas columnas que uno se pierde | La tarjeta muestra sólo lo que hace falta para decidir; el resto está en el detalle |
| Los siniestros ya terminados tapan a los que faltan | Apenas se marca **Facturado**, el siniestro desaparece de la página |
| Hay que volver a cargar todo a mano en el Excel original | Exporta un `.xlsx` con **las mismas 14 columnas**, en el mismo orden |

---

## Cómo se usa (día a día)

1. **Bajar la tarea de RUS** — desde el sistema de Río Uruguay, el archivo
   `TareaAsignada.xls` de siempre.
2. **Actualizar lista** — arrastrar el archivo al recuadro.
3. **Mirar el resumen.** Aparece algo así:

   > Se van a agregar **7 siniestros nuevos**. Los otros **29** ya los tenías,
   > así que no se duplican.

   En las solapas están los números uno por uno: los que faltaban, los que ya
   estaban, los que vienen repetidos dentro del propio archivo y los que
   cambiaron de estado o de vencimiento.
4. **Agregar los que faltan.** Sólo entran los nuevos. Si te equivocaste de
   archivo, hay un botón **Deshacer** por unos segundos.
5. **Trabajar la lista.** Tocá **Lo revisé** cada vez que entrás a un siniestro:
   ése es el dato que después te dice cuáles se están quedando atrás.
6. **Exportar** cuando quieras pasarlo al Excel original:
   - *Sólo los nuevos* → para pegarlos debajo, sin tocar el resto.
   - *Igual a tu planilla* → la planilla completa con las mismas columnas.

---

## Las pantallas

**El tablero de arriba son los filtros.** Tocá cualquiera para filtrar:

- **En curso** — lo que todavía no se facturó. Es lo que se ve al entrar.
- **Urgentes** — vencidos, por vencer o abandonados hace rato.
- **Terceros** — los que más se escapan.
- **Sin revisar** — hace más días de los que configuraste.
- **Por facturar** — informe hecho y falta facturar. Plata en la calle.

### Cuándo desaparece un siniestro

Cuando se marca **Facturado**. Ése es el final del circuito: la tarjeta se va
de la página en el acto y no vuelve a aparecer en el día a día.

**Dónde quedan.** En **Configuración → Ver los N facturados**. No se borra
nunca nada. Si marcaste uno sin querer, entrás ahí, destildás *Facturado* y
vuelve solo a la lista.

También los encontrás **buscando por número**: el buscador ignora los filtros
y mira la lista entera, facturados incluidos.

El **cierre solo no alcanza**. Si está cerrado pero todavía no se facturó,
sigue a la vista, porque es plata por cobrar. (En la planilla original hay 79
siniestros facturados sin el cierre marcado y sólo 4 al revés, así que el que
manda es *Facturado*.)

Si en el export de RUS el estado dice *cerrada*, *finalizada* o *anulada*,
también se considera terminado.

Buscar por número **encuentra todo**, esté terminado o no: el buscador ignora
el filtro. Y el chip **Ver todos**, al lado del buscador, muestra la lista
entera.

**Cada tarjeta** trae el número de siniestro (con botón para copiarlo), el
vehículo, el contador de días sin revisar, y los tres pasos —**Informe →
Cierre → Facturado**— que se marcan tocándolos.

**Abriendo el detalle** se editan los datos, se escriben notas ("llamar al
taller el lunes") y se ve el historial de todo lo que se fue haciendo.

---

## Vincular la planilla

En Chrome o Edge se puede **vincular** el Excel una sola vez: después alcanza
con tocar **Sincronizar** y lo vuelve a leer sin buscar el archivo. También
puede escribir de vuelta en ese mismo archivo, avisando antes.

Un detalle importante: el navegador **no puede vigilar un archivo solo**. Por
seguridad, siempre hace falta un clic. "Automático" acá quiere decir *un clic*,
no que se actualice de fondo.

---

## Formatos que lee

- `.xls` de RUS — el binario viejo de Excel, que es el que baja el sistema
- `.xlsx` — Excel moderno
- `.csv` — con `;` o `,`, detecta solo cuál es
- Filas **pegadas** directamente desde Excel (Ctrl+C / Ctrl+V)

Reconoce solo dos planillas y sabe qué es cada columna:

- **Export de RUS · Tareas asignadas** (`NUMERO SINIESTRO`, `FECHA VENCIMIENTO`,
  `TIPO DE RECLAMO`, `PRIORIDAD`…)
- **Planilla de seguimiento propia** (`Siniestro`, `Fecha deriv`, `Dominio`,
  `Aseg o terc`, `INFORME`, `CIERRE`, `FACTURADO`…)

Si aparece cualquier otra planilla, la intenta reconocer por el nombre de las
columnas y, si no puede, abre una pantalla para asignarlas a mano.

### Cómo decide si un siniestro está repetido

Compara el **número de siniestro** normalizado: le saca el `.0` que agrega
Excel, los espacios, los guiones y los ceros de la izquierda. Así `1736879`,
`1736879.0` y `01736879` cuentan como el mismo.

Cuando el mismo número ya existe, **nunca lo duplica**: sólo refresca lo que
manda RUS (vencimiento, estado, prioridad). Tus notas, tus marcas de informe,
cierre y facturado, y las fechas de revisión **no se pisan nunca**.

---

## Dónde quedan los datos

En el navegador de esa computadora (`localStorage`). **No se suben a ningún
lado**, no hay servidor ni base de datos.

Consecuencia: si cambiás de máquina o de navegador, los datos no viajan solos.
Usá **Exportar → Bajar respaldo completo (.json)** y después **Restaurar** del
otro lado. El respaldo incluye las notas y las fechas de revisión, que no van
en el Excel.

> Conviene bajar un respaldo de vez en cuando. Si alguien limpia los datos de
> navegación del navegador, se borra todo. **Éste es el riesgo real, no el
> espacio.**

### ¿Cuánto ocupa?

Con 196 siniestros cargados: **101 KB**. El tope del navegador ronda los 5 MB,
así que se usa un 2 %. En *Configuración → Espacio usado* hay una barra que lo
muestra.

A un ritmo de unos 200 siniestros por año, la proyección a 10 años (2.000
siniestros, 15 revisiones cada uno) da **2,27 MB: el 45 % del tope**. Con eso
alcanza para más de 20 años.

Dos decisiones que lo mantienen chico:

- **No se guardan los campos vacíos.** La planilla tiene columnas que casi no
  se usan (KM, tramitador, fecha de ofrecimiento); guardarlas vacías era más de
  la mitad del archivo. Sacarlas achicó todo un 40 %.
- **El historial no crece sin freno.** Marcar *Lo revisé* varias veces el mismo
  día actualiza la última anotación en vez de sumar una nueva, y cada siniestro
  guarda como mucho 40 movimientos. Doscientos clics en un día dejan 2
  anotaciones, no 201.

---

## Publicarlo en Vercel

```bash
npm i -g vercel
vercel            # primera vez, para previsualizar
vercel --prod     # cuando esté listo
```

O desde [vercel.com](https://vercel.com): **Add New → Project**, elegir este
repositorio y **Deploy**. No hay que configurar nada: no tiene build, es un
archivo estático.

También funciona en GitHub Pages, Netlify, o abriendo `index.html` con doble
clic (en ese caso no anda vincular la planilla, que necesita `https`).

---

## Cómo está armado

Todo en `index.html`, sin dependencias, dividido en secciones marcadas con
comentarios:

| Sección | Qué hace |
|---|---|
| `CFB / OLE` | Abre el contenedor de los `.xls` viejos |
| `BIFF8` | Lee las celdas de adentro: textos, números, fechas |
| `XLSX` | Descomprime el ZIP y parsea el XML de los `.xlsx` |
| `ESCRITOR` | Arma el `.xlsx` de salida (ZIP + XML + CRC32) |
| `MODELO` | Normalización, fechas y el cálculo de urgencia |
| `IMPORTAR` | Reconoce columnas, cruza y deduplica |
| `VISTA` / `PANEL` / `FLUJOS` | Todo lo que se ve |

Los lectores de Excel están escritos a mano justamente para que el archivo sea
uno solo y no dependa de ninguna CDN. Se validaron celda por celda contra
`openpyxl` y `xlrd`: 15.464 celdas, sin diferencias.
