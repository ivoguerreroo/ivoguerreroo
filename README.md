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
| Se pierde el Excel manual, con todo el trabajo de tenerlo al día | La app reemplaza esa planilla; no hace falta mantenerla más |

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
6. **Exportar** cuando necesites un `.xlsx` o `.csv` para imprimir, mandar por
   mail o archivar. La app es la que lleva la lista de ahora en más — no hace
   falta mantener un Excel aparte ni copiar nada de vuelta a ningún lado.

---

## Las pantallas

**El tablero de arriba son los filtros.** Tocá cualquiera para filtrar:

- **En curso** — lo que todavía no se facturó. Es lo que se ve al entrar.
- **Aseg. / CLEAS** — asegurado propio y convenio, en curso.
- **Terceros** — los que más se escapan.
- **Sin revisar** — hace más días de los que configuraste.
- **Por facturar** — informe hecho y falta facturar. Plata en la calle.

Lo urgente no necesita ficha propia: el orden por defecto de las tarjetas ya
pone adelante lo vencido y lo abandonado.

### Cuándo desaparece un siniestro

Cuando marcás **Informe** y **Cierre**, o cuando marcás **Facturado**. Con
cualquiera de los dos, la tarjeta se va de la página en el acto.

La diferencia es a dónde va:

- **Informe + Cierre, sin facturar** → queda visible en la ficha **Por
  facturar** del tablero. Es plata que ya podés cobrar; no se esconde.
- **Facturado** → sale de la vista del todo y queda guardado en
  **Configuración → Terminados**.

**Nada se borra nunca.** En Configuración → Terminados podés buscar cualquiera
y destildar el paso que corresponda para que vuelva a la lista. También los
encontrás **buscando por número**: el buscador ignora los filtros y mira la
lista entera, terminados incluidos.

Si en el export de RUS el estado dice *cerrada*, *finalizada* o *anulada*,
también se considera terminado.

**Cada tarjeta** muestra lo mínimo para decidir sin cansar la vista: número de
siniestro (con botón para copiarlo), vehículo, si es de tercero o de asegurado,
los tres pasos —**Informe → Cierre → Facturado**— que se marcan tocándolos, y
una línea con las fechas. El vencimiento se lee solo: dice *Venció el* en rojo o
*Vence el* según corresponda, sin cartelitos aparte.

Arriba a la derecha, una pastilla dice hace cuánto que no se mira: gris cuando
está al día, ámbar cuando pasó el plazo configurado.

Si el siniestro tiene un celular cargado, aparece un **botón de WhatsApp**
verde bien visible que abre el chat con esa persona — en la tarjeta y en el
detalle. Los teléfonos fijos y los mails que a veces quedan en esa columna no
generan botón, porque WhatsApp no funcionaría.

**Abriendo el detalle** están todos los datos en un solo bloque y **todos se
pueden editar**, incluso los que llegaron de RUS: si algo vino mal, se corrige a
mano. El tramitador se completa solo con el emisor que manda RUS (que es la
misma persona que figura como dueño del siniestro, sólo que sin el usuario
adelante). Abajo van las notas propias ("llamar al taller el lunes") y el
historial de todo lo que se fue haciendo.

Lo que RUS manda pero no aporta al seguimiento — nombre de la tarea, tipo de
reclamo, plazo, estado y usuario que lo ingresó — no se muestra. Se sigue
guardando igual, porque de ahí sale si el siniestro es de tercero o de
asegurado.

---

## Vincular el archivo de RUS

En Chrome o Edge se puede **vincular** el archivo que bajás de RUS
(`TareaAsignada.xls`) una sola vez: después alcanza con tocar **Sincronizar**
y lo vuelve a leer sin que lo tengas que buscar cada semana.

Un detalle importante: el navegador **no puede vigilar un archivo solo**. Por
seguridad, siempre hace falta un clic. "Automático" acá quiere decir *un clic*,
no que se actualice de fondo.

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
manda RUS (vencimiento, estado, prioridad). Tus notas, tus marcas y las fechas
de revisión **no se pisan nunca**.

### Las marcas de la planilla sí se importan

`INFORME`, `CIERRE` y `FACTURADO` se traen tal cual vienen del Excel. Eso es lo
que hace que al importar los 189 siniestros históricos queden a la vista sólo
los **38 que están abiertos**: los ~150 ya cobrados entran directo a Facturados
y no molestan.

Si alguna vez hace falta empezar de cero, en **Configuración → Facturados** hay
un botón para desmarcarlos todos de una. No borra siniestros, ni notas, ni
fechas de revisión: sólo la marca.

---

## Dónde quedan los datos

En el navegador de esa computadora (`localStorage`). **No se suben a ningún
lado**, no hay servidor ni base de datos.

Consecuencia: si cambiás de máquina o de navegador, los datos no viajan solos.
Usá **Exportar → Bajar respaldo completo (.json)** y después **Restaurar** del
otro lado. El respaldo incluye las notas y las fechas de revisión, que no van
en el `.xlsx` que exportás.

> Conviene bajar un respaldo de vez en cuando. Si alguien limpia los datos de
> navegación del navegador, se borra todo. **Éste es el riesgo real, no el
> espacio.**

### Respaldo automático por mail

La app puede mandar el respaldo `.json` por mail sola, cada 7 días, como
adjunto. El archivo del script está en `apps-script/respaldo.gs`.

**Antes que nada, una aclaración que conviene entender.** Una página web no
puede mandar mails por su cuenta: no tiene servidor ni credenciales, y los
datos viven en el navegador de quien la usa. Por eso el envío lo dispara el
navegador **al abrir la página**, contra un Google Apps Script que sí tiene
permiso de enviar. En la práctica: la primera vez que se abre la app después de
una semana, sale el respaldo. Con la compu apagada no se manda nada, pero
tampoco hace falta — si nadie la abrió, los datos no cambiaron.

Se eligió Apps Script porque es gratis, no pide dominio propio ni tarjeta, y el
mail sale de una cuenta de Gmail que ya se tiene.

**Cómo se configura (una sola vez, unos 5 minutos):**

1. Entrá a [script.google.com](https://script.google.com) → **Nuevo proyecto**.
2. Borrá lo que aparezca y pegá todo el contenido de `apps-script/respaldo.gs`.
3. Arriba de ese archivo hay dos líneas para tocar:
   - `DESTINO` — a qué mail llega. Ya viene con el de destino puesto.
   - `CLAVE` — cambiala por cualquier frase inventada.
4. **Implementar → Nueva implementación → Aplicación web**, con
   *Ejecutar como: Yo* y *Quién tiene acceso: Cualquier usuario*.
5. Autorizá los permisos (es tu propia cuenta) y copiá la URL que termina en
   `/exec`.
6. En la app: **Configuración → Respaldo automático**, pegá la URL, escribí la
   misma clave, activá la casilla y tocá **Mandar uno de prueba ahora**.

Si el mail de prueba llega, ya está andando.

**Si la página se abre con doble clic, esto no va a andar.** El navegador bloquea
el envío desde un archivo local, y el método de emergencia que queda
(`sendBeacon`) tiene un tope de 50 KB — un respaldo de 200 siniestros pesa el
doble. La app lo detecta y lo avisa con los números concretos en pantalla. Para
que el respaldo por mail funcione de verdad hay que **subir la página a Vercel**.

**Dos decisiones de seguridad:**

- El mail de destino está **fijo dentro del script**, no lo manda la página.
  Aunque alguien descubra la URL, no puede usar el servicio para mandar mails a
  otro lado.
- **La clave y la URL no viajan en el respaldo.** Esos mails quedan guardados
  para siempre en una casilla y no corresponde que lleven una credencial
  adentro. Al restaurar en otra máquina hay que volver a pegarlas.

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
clic (en ese caso no anda vincular el archivo de RUS, que necesita `https`).

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
