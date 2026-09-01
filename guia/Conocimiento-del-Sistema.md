# Radar de Siniestros — Base de conocimiento para Claude

Este documento describe, con precisión, cómo funciona por dentro el sistema
"Radar de Siniestros" que usa **Walter Guerrero** para llevar el seguimiento
de sus siniestros de **Río Uruguay Seguros**. Fue extraído directamente del
código de la página, no es una aproximación.

**Instrucciones para vos, Claude, si estás leyendo esto para responder a
Walter:** contestá en español rioplatense, de "vos", con oraciones cortas y
sin tecnicismos — Walter no es programador, usa la página desde el navegador
y antes llevaba todo esto a mano en un Excel. Si una pregunta tiene que ver
con "por qué desapareció tal siniestro" o "qué hago para que vuelva",
respondé con la regla exacta de este documento, no adivines. Si Walter
describe algo que no coincide con estas reglas (por ejemplo dice que algo no
se movió cuando debería haberse movido), lo más probable es que le falte un
paso (ver la sección de dudas típicas) — preguntale qué exactamente tocó
antes de asumir que es un error del sistema.

---

## 1. Los tres pasos: Informe, Cierre, Facturado

Cada siniestro tiene tres círculos para tocar: **Informe → Cierre →
Facturado**. Son independientes entre sí (marcar uno no marca los otros
solos), y lo que hacen es:

| Marcaste... | Qué pasa |
|---|---|
| Sólo **Informe** | No pasa nada más que quedar marcado. El siniestro sigue en "En curso", a la vista. |
| **Informe + Cierre** (sin Facturado) | El siniestro **sale de "En curso"** — pero no se pierde: pasa a la ficha **"Por facturar"** del tablero, que sigue visible. Es la señal de "ya está resuelto, falta cobrar". |
| **Facturado** (con o sin Cierre marcado) | El siniestro **desaparece de la vista normal por completo**. Queda guardado en **Configuración → Terminados**. Alcanza con marcar sólo Facturado — no hace falta tener Cierre tildado también. |

Un siniestro también se considera terminado automáticamente, sin que Walter
toque nada, si el **estado que manda RUS** dice *cerrada*, *finalizada*,
*anulada* o *rechazada*.

**Nada se borra nunca.** Marcar un paso sólo cambia dónde se ve el
siniestro, no lo elimina. Para deshacer cualquiera de los tres, hay que
buscar el siniestro (el buscador encuentra los terminados también, ver
sección 5) y destildar el paso: vuelve solo a la lista de "En curso".

### El botón "Reabrir los N" de Configuración

En **Configuración → Terminados** hay un botón rojo que dice "Empezar de
cero: reabrir los N". Esto **desmarca Informe, Cierre y Facturado de todos
los terminados a la vez** — está pensado para arrancar de cero con la lista
completa, no para el uso del día a día. No borra ningún siniestro, ni notas,
ni fechas de revisión: sólo esas tres marcas.

---

## 2. El tablero de arriba (los 5 recuadros)

| Ficha | Qué cuenta |
|---|---|
| **En curso** | Todo lo que todavía no cumple ninguna de las condiciones de "terminado" de la sección 1. Es lo que se ve al entrar a la página. |
| **Aseg. / CLEAS** | De los "en curso", los que son categoría Asegurado o CLEAS. |
| **Terceros** | De los "en curso", los que son de terceros. |
| **Sin revisar** | De los "en curso", los que hace más días de la cuenta que nadie los abre. El plazo se configura (por defecto 12 días para los comunes, 7 días para los de tercero — los de tercero se controlan más seguido porque son los que más se escapan). |
| **Por facturar** | Informe **y** Cierre marcados, pero Facturado todavía no. Es la plata que ya se puede cobrar. |

No están en el tablero, pero existen: **Urgentes** (los de mayor puntaje de
urgencia — se llega ahí sólo internamente, el orden por defecto de las
tarjetas ya los pone primero) y **Terminados** (se llega desde Configuración,
ver sección 1).

---

## 3. La pastilla "hace cuánto no lo mirás"

Arriba a la derecha de cada tarjeta hay una pastilla chica:

- **Gris**, dice "sin ver" → nunca se abrió ese siniestro.
- **Gris**, dice "visto hoy" → se revisó hoy mismo.
- **Verde**, dice "hace X días" → se revisó hace poco, todavía dentro del plazo.
- **Ámbar/naranja**, dice "hace X días" → pasó el plazo configurado (12 o 7
  días según el tipo) sin que nadie lo mirara.

Se actualiza tocando el botón **"Lo revisé"** — eso anota la fecha de hoy
como última revisión. Si se toca varias veces el mismo día, no se acumula:
sólo cuenta la última vez.

---

## 4. El color del borde de cada tarjeta (franja izquierda)

Es el nivel de urgencia general del siniestro, calculado con un puntaje:

- **Rojo** (crítico, puntaje 70 o más): está vencido, vence hoy o en muy
  pocos días, o combina varias señales de atraso.
- **Naranja** (atención, puntaje entre 28 y 69): alguna señal de que hay que
  mirarlo pronto, pero no es urgente todavía.
- **Verde** (bien, puntaje menor a 28): tranquilo por ahora.
- **Gris apagado** (terminado): ya está resuelto — sólo se ve en la sección
  "Por facturar" o dentro de "Terminados", nunca en "En curso".

### Qué suma puntaje (de más a menos peso)

- Vencido: sube mucho, y sigue subiendo cuantos más días pasaron.
- Vence hoy, o en 1-2 días, o en 3-5 días: suma bastante, cada vez menos.
- Hace más del plazo configurado que no se revisa: suma, más cuanto más
  tiempo pasó.
- Nunca se revisó: suma un poco extra.
- Es de tercero: siempre suma un poco (por eso los de tercero tienden a
  aparecer más arriba en la lista).
- Prioridad "Alta" (la que manda RUS): suma un poco.
- Fue derivado hace más de 15 días y todavía no tiene Informe: suma bastante.

El orden **"Más urgente primero"** (el que viene elegido por defecto) ordena
la lista por este puntaje, de mayor a menor.

---

## 5. El buscador

Busca por **número de siniestro, patente, vehículo, teléfono y notas**.

Punto importante: **el buscador ignora cualquier filtro que esté activo y
mira la lista completa**, incluidos los siniestros ya terminados o
facturados. Si Walter necesita encontrar uno viejo que ya cerró, escribiendo
el número (o parte de la patente, etc.) lo va a encontrar igual, sin
importar en qué pestaña o filtro esté parado.

---

## 6. Tercero, Asegurado o CLEAS — cómo lo decide el sistema

Cuando se importa un siniestro, el sistema adivina la categoría así, en
este orden:

1. Mira la columna "Aseg o terc" tal cual viene en la planilla: si dice
   algo con "cleas" → **CLEAS**. Si dice "3ro", "3ero", o cualquier variante
   de "tercer..." → **Tercero**. Si dice algo con "aseg" → **Asegurado**.
2. Si esa columna no ayuda, mira el tipo de reclamo o el nombre de la tarea
   que manda RUS: "RC cosas", "responsabilidad civil" o menciones a
   terceros → **Tercero**. "Daño parcial", "daño total", "todo riesgo",
   "Cesvicom" → **Asegurado**.

Si el sistema se equivocó, se puede corregir a mano abriendo el detalle del
siniestro y cambiando el desplegable — queda guardado tal cual lo deje
Walter, no se vuelve a pisar solo.

---

## 7. Importar la planilla — qué pasa con los repetidos

Al tocar "Actualizar lista" y soltar un archivo (el `.xls` que baja de RUS,
o la propia planilla de seguimiento), el sistema compara **por número de
siniestro**, después de "limpiarlo": le saca el `.0` que agrega Excel, deja
sólo letras y números, y saca los ceros de más a la izquierda. Así
`1736879`, `1736879.0` y `01736879` cuentan como el mismo número.

- **Si el número ya existe en la lista**: nunca se duplica. Si el archivo
  trae datos nuevos donde antes había un campo vacío, o algo cambió (por
  ejemplo la fecha de vencimiento), se actualiza ese campo puntual — pero
  **nunca pisa algo que ya estaba escrito** con un dato entrante vacío.
  Las notas propias y las fechas de revisión de Walter nunca se pisan por
  una importación.
- **Si el mismo número aparece dos veces dentro del propio archivo** que se
  está importando, sólo se toma la primera vez que aparece.
- **Si es un número nuevo**, se agrega a la lista.

Antes de confirmar, la pantalla muestra cuántos van a ser nuevos, cuántos ya
estaban, cuántos vienen repetidos dentro del mismo archivo, y cuántos
cambiaron algún dato — con la lista de números en cada categoría.

Después de importar, aparece un botón **"Deshacer"** por unos segundos: si
Walter se equivocó de archivo, saca justo lo que se acababa de agregar (sin
tocar lo que ya estaba).

---

## 8. El botón de WhatsApp

Aparece un botón verde (en la tarjeta y también adentro del detalle) sólo
si el teléfono cargado es reconocible como un celular argentino. El sistema
arma el link automáticamente, sin importar si el número se cargó con el 0
adelante, con guiones, con o sin el 15 viejo, etc.

**No aparece** si en esa columna hay un mail, un teléfono fijo de 7 dígitos
sin código de área, o cualquier texto que no sea un número de celular
válido — esos casos existen en los datos reales (algunas filas de la
planilla tienen el mail del cliente en la columna de teléfono) y el sistema
los descarta en vez de armar un link que no funcionaría.

---

## 9. El respaldo automático por mail

Se configura una sola vez en **Configuración → Respaldo automático**: hay
que pegar el link del script de Google (el que termina en `/exec`), la
clave que se puso en ese script, y activar la casilla.

Cómo funciona en la práctica:

- Se manda **al abrir la página**, si ya pasaron 7 días (o los que se hayan
  configurado) desde el último envío. No es un reloj que corre solo con la
  compu apagada — si nadie abre la página, no sale nada, pero tampoco hay
  datos nuevos que respaldar en ese caso.
- Si el respaldo automático **no** está activado, cada 14 días sin bajar uno
  a mano el sistema avisa igual, para no perder la costumbre.
- **Ojo con esto:** si la página se abre haciendo doble clic en el archivo
  (en vez de entrar por una dirección de internet), el envío puede fallar
  por una restricción de seguridad del navegador. Hay un método de
  emergencia que a veces lo salva, pero tiene un límite de 50 KB — con
  muchos siniestros cargados el respaldo pesa más que eso y ese método
  tampoco alcanza. La solución firme es tener la página **subida a
  internet** (por ejemplo en Vercel), no abrirla como archivo suelto.

---

## 10. Dónde viven los datos

Todo queda guardado **en el navegador de esa computadora** (una tecnología
que se llama `localStorage`). No hay servidor, no hay nube: nadie más que
esa máquina tiene esos datos, y no hace falta internet para que la página
funcione en el día a día (sólo para importar un archivo o mandar el
respaldo por mail, que son acciones puntuales).

Consecuencia importante: si se abre la página desde **otra computadora o
navegador**, ahí no van a estar los mismos datos — hay que restaurar un
respaldo. Por eso conviene bajar uno de vez en cuando desde "Exportar →
Bajar respaldo completo (.json)", además del automático por mail.

---

## 11. Exportar

Desde el botón "Exportar" se puede bajar:

- Un `.xlsx` con las columnas de siempre, para abrir en Excel.
- Un `.xlsx` con los datos de RUS agregados también.
- Un `.csv`.
- Un respaldo completo en `.json`, que además de los datos de la planilla
  incluye las notas propias y las fechas de revisión (esas dos cosas no
  van en el Excel).

---

## 12. Vincular el archivo de RUS

Sólo funciona en Chrome o Edge, y sólo si la página está en una dirección
de internet (no abierta como archivo suelto). Se elige el archivo una vez
y después, con el botón "Sincronizar", se vuelve a leer sin tener que
buscarlo cada semana. Esto **no** hace que se actualice solo sin tocar
nada — siempre hace falta un clic en "Sincronizar".

---

## Dudas típicas (para responder rápido)

**"Marqué Informe y Cierre y el siniestro no se movió."**
Fijate si de verdad quedaron los dos marcados (a veces uno se toca dos
veces y termina desmarcado). Si los dos están marcados y sigue en "En
curso", puede ser que ya estuviera facturado o que RUS lo haya dado de baja
por otro motivo — buscalo por número y mirá el detalle.

**"No encuentro un siniestro que sé que existe."**
Escribilo en el buscador de arriba: encuentra todo, esté terminado o no,
sin importar el filtro activo.

**"Marqué Facturado sin querer."**
Andá a Configuración → "Ver los N terminados", buscá el número, y
destildá Facturado. Vuelve solo a la lista. No se pierde nada.

**"¿Por qué este siniestro aparece más arriba que otro que venció antes?"**
El orden por defecto no es sólo por fecha de vencimiento: combina varias
señales (ver sección 4). Un tercero sin revisar hace muchos días puede
aparecer antes que uno vencido si el segundo se revisó hoy.

**"Actualicé la lista y no se agregó nada."**
Es normal si todos los números del archivo ya estaban cargados — el
sistema avisa "ya los tenías, no se duplican" y no hace falta hacer nada
más.

**"No me llegó el mail del respaldo."**
Ver la sección 9 — lo más común es que la página esté abierta como archivo
suelto en vez de por internet, o que todavía no hayan pasado los 7 días.

**"¿Se puede perder todo?"**
Sí, si se borran los datos de navegación de ese navegador (por ejemplo
"limpiando" el Chrome). Por eso existen los respaldos — conviene tener
alguno reciente siempre.
