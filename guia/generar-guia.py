import base64, os
D = 'manual'
def img(n):
    return 'data:image/png;base64,' + base64.b64encode(open(f'{D}/{n}.png','rb').read()).decode()

CSS = """
@page { size: A4; margin: 0; }
*{box-sizing:border-box;margin:0;padding:0}
body{
  font-family:"Liberation Sans","DejaVu Sans",Arial,sans-serif;
  color:#16202e; -webkit-print-color-adjust:exact; print-color-adjust:exact;
}
.hoja{
  width:210mm;height:297mm;padding:16mm 15mm;position:relative;
  page-break-after:always;overflow:hidden;background:#fff;
}
.hoja:last-child{page-break-after:auto}

/* --- portada --- */
.portada{background:linear-gradient(160deg,#12315e 0%,#1e5eb8 55%,#3f7fd6 100%);color:#fff;padding:0}
.portada-int{padding:26mm 18mm;height:100%;display:flex;flex-direction:column}
.logo{width:19mm;height:19mm;border-radius:5mm;background:rgba(255,255,255,.16);
  display:flex;align-items:center;justify-content:center;margin-bottom:9mm;
  border:1.5px solid rgba(255,255,255,.35)}
.logo svg{width:11mm;height:11mm}
.portada h1{font-size:32pt;font-weight:800;letter-spacing:-.02em;line-height:1.05}
.portada .sub{font-size:15pt;opacity:.85;margin-top:3mm;font-weight:400}
.portada .frase{font-size:11.5pt;opacity:.8;margin-top:7mm;line-height:1.6;max-width:120mm}
.portada .marco{
  margin-top:auto;border-radius:3mm;overflow:hidden;
  box-shadow:0 8mm 22mm rgba(0,0,0,.4);border:1px solid rgba(255,255,255,.25);
}
.portada .marco img{width:100%;display:block}
.pie-portada{margin-top:7mm;font-size:9.5pt;opacity:.7}

/* --- encabezado de pagina --- */
.cinta{display:flex;align-items:center;gap:4mm;margin-bottom:7mm}
.cinta .num{
  width:9mm;height:9mm;border-radius:50%;background:#1e5eb8;color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:13pt;font-weight:800;flex:none;
}
.cinta h2{font-size:19pt;font-weight:800;letter-spacing:-.02em;line-height:1.1}
.cinta p{font-size:10.5pt;color:#5a6b85;margin-top:.8mm}

/* --- captura: los numeritos van en los margenes, nunca encima --- */
.captura{position:relative;padding:0 9.5mm}
.foto{position:relative;border-radius:2.5mm;overflow:hidden;border:1px solid #d6dee9;
  box-shadow:0 2mm 7mm rgba(16,24,40,.13)}
.foto img{width:100%;display:block}
.punto{
  position:absolute;width:7.5mm;height:7.5mm;border-radius:50%;
  background:#e8362f;color:#fff;font-size:10.5pt;font-weight:800;
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 0 0 1.2mm #fff, 0 .8mm 2.5mm rgba(0,0,0,.3);
  transform:translate(-50%,-50%);z-index:3;
}
.izq{left:4.7mm;transform:translate(-50%,-50%)}
.der{right:4.7mm;transform:translate(50%,-50%)}
/* el aro marca el objetivo, sin taparlo */
.aro{
  position:absolute;border:.9mm solid #e8362f;border-radius:2mm;
  transform:translate(-50%,-50%);box-shadow:0 0 0 .8mm rgba(255,255,255,.9);z-index:2;
}

/* --- lista de referencias --- */
.refs{margin-top:6mm;display:grid;grid-template-columns:1fr 1fr;gap:3.5mm 7mm}
.refs.una{grid-template-columns:1fr}
.ref{display:flex;gap:3mm;align-items:flex-start}
.ref .n{
  width:6.5mm;height:6.5mm;border-radius:50%;background:#e8362f;color:#fff;flex:none;
  font-size:9.5pt;font-weight:800;display:flex;align-items:center;justify-content:center;margin-top:.3mm;
}
.ref b{display:block;font-size:11pt;font-weight:700;margin-bottom:.7mm}
.ref span{font-size:10pt;color:#4a5a72;line-height:1.45}

/* --- pasos grandes --- */
.pasos-grandes{display:flex;flex-direction:column;gap:6mm;margin-top:4mm}
.paso-g{display:flex;gap:6mm;align-items:center;background:#f5f8fc;border:1px solid #e2eaf4;
  border-radius:3mm;padding:7mm 8mm}
.paso-g .bola{
  width:16mm;height:16mm;border-radius:50%;background:#1e5eb8;color:#fff;flex:none;
  font-size:21pt;font-weight:800;display:flex;align-items:center;justify-content:center;
}
.paso-g h3{font-size:14pt;font-weight:750;margin-bottom:1.5mm}
.paso-g p{font-size:11pt;color:#4a5a72;line-height:1.5}

/* --- avisos --- */
.nota{
  margin-top:6mm;padding:5mm 6mm;border-radius:2.5mm;font-size:10.5pt;line-height:1.55;
  background:#fff8e6;border:1px solid #f0dcb0;color:#5c4813;
}
.nota.ok{background:#eaf7f0;border-color:#bfe3d0;color:#14532d}
.nota b{font-weight:750}

.dosfotos{display:flex;gap:6mm;align-items:flex-start}
.dosfotos .captura{flex:1}

.pie{position:absolute;bottom:9mm;left:15mm;right:15mm;display:flex;justify-content:space-between;
  font-size:8.5pt;color:#98a5b8;border-top:1px solid #e6ecf4;padding-top:3mm}
"""

LOGO = ('<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M19.07 4.93A10 10 0 1 1 6.99 3.34"/><path d="M12 12 16 8"/>'
        '<circle cx="12" cy="12" r="4"/></svg>')

def pie(n, txt='Radar de Siniestros · Guía rápida'):
    return f'<div class="pie"><span>{txt}</span><span>{n}</span></div>'

def refs(items, una=False, desde=1):
    cls = 'refs una' if una else 'refs'
    h = f'<div class="{cls}">'
    for i,(t,d) in enumerate(items,desde):
        h += f'<div class="ref"><div class="n">{i}</div><div><b>{t}</b><span>{d}</span></div></div>'
    return h + '</div>'

html = f"""<!doctype html><html lang="es-AR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>

<!-- 1. PORTADA -->
<section class="hoja portada"><div class="portada-int">
  <div class="logo">{LOGO}</div>
  <h1>Radar de<br>Siniestros</h1>
  <div class="sub">Guía rápida para usarlo</div>
  <div class="frase">Reemplaza la planilla de Excel. Muestra sólo los siniestros que
  siguen abiertos y avisa cuáles hace rato que no mirás.</div>
  <div class="marco"><img src="{img('principal')}"></div>
  <div class="pie-portada">Hecho para Walter Guerrero · Río Uruguay Seguros</div>
</div></section>

<!-- 2. EL DIA A DIA -->
<section class="hoja">
  <div class="cinta"><div class="num">1</div><div>
    <h2>El día a día, en 3 pasos</h2>
    <p>No hace falta hacer nada más que esto</p></div></div>

  <div class="pasos-grandes">
    <div class="paso-g"><div class="bola">1</div><div>
      <h3>Abrí la página</h3>
      <p>Lo que ves son los siniestros que <b>todavía no cobraste</b>.
      Los ya facturados no aparecen: están guardados aparte.</p></div></div>

    <div class="paso-g"><div class="bola">2</div><div>
      <h3>Mirá los primeros de la lista</h3>
      <p>Siempre aparecen arriba los más urgentes: los vencidos y los que
      hace más días que no tocás. Si atendés los de arriba, no se te escapa ninguno.</p></div></div>

    <div class="paso-g"><div class="bola">3</div><div>
      <h3>Tocá "Lo revisé"</h3>
      <p>Cada vez que entrás a un siniestro, tocá ese botón. Así el sistema
      sabe que lo miraste hoy y deja de marcarlo como atrasado.</p></div></div>
  </div>

  <div class="nota ok"><b>Todo se guarda solo.</b> No hay que apretar ningún botón de
  guardar: apenas tocás algo, ya queda registrado.</div>

  <div class="nota"><b>Una vez por semana</b> conviene traer los siniestros nuevos
  desde RUS. Está explicado en la página 5.</div>

  {pie(2)}
</section>

<!-- 3. LA PANTALLA PRINCIPAL -->
<section class="hoja">
  <div class="cinta"><div class="num">2</div><div>
    <h2>La pantalla principal</h2>
    <p>Qué es cada cosa</p></div></div>

  <div class="captura">
    <div class="foto"><img src="{img('principal')}">
      <div class="aro" style="left:71.5%;top:4.2%;width:24%;height:7.5%"></div>
      <div class="aro" style="left:96.3%;top:4.2%;width:6.5%;height:7.5%"></div>
      <div class="aro" style="left:50%;top:17.5%;width:97%;height:15%"></div>
      <div class="aro" style="left:31%;top:30%;width:58%;height:7%"></div>
      <div class="aro" style="left:50%;top:67.5%;width:97%;height:64%"></div>
    </div>
    <div class="punto der" style="top:3%">1</div>
    <div class="punto der" style="top:9%">5</div>
    <div class="punto izq" style="top:17.5%">2</div>
    <div class="punto izq" style="top:30%">3</div>
    <div class="punto izq" style="top:62%">4</div>
  </div>

  {refs([
    ("Actualizar lista","Para traer los siniestros nuevos que bajaste de RUS."),
    ("Los 5 recuadros","Son filtros. Tocá uno y la lista muestra sólo eso."),
    ("Buscador","Escribí un número de siniestro o una patente y lo encuentra, aunque ya esté facturado."),
    ("Las tarjetas","Un siniestro cada una. Están explicadas en la página siguiente."),
    ("Configuración","Ahí están los facturados y los avisos."),
  ])}

  <div class="nota"><b>Los 5 recuadros de arriba:</b> <b>En curso</b> es todo lo que falta cobrar ·
  <b>Aseg./CLEAS</b> y <b>Terceros</b> separan por tipo · <b>Sin revisar</b> son los que hace
  mucho no mirás · <b>Por facturar</b> es plata que ya podés cobrar.</div>

  {pie(3)}
</section>

<!-- 4. LA TARJETA -->
<section class="hoja">
  <div class="cinta"><div class="num">3</div><div>
    <h2>Cada tarjeta</h2>
    <p>Un siniestro, todo lo que hace falta para decidir</p></div></div>

  <div style="display:flex;gap:8mm;align-items:flex-start">
    <div class="captura" style="width:104mm;flex:none">
      <div class="foto"><img src="{img('tarjeta')}">
        <div class="aro" style="left:20%;top:10%;width:34%;height:12%"></div>
        <div class="aro" style="left:83%;top:9.5%;width:30%;height:11%"></div>
        <div class="aro" style="left:15%;top:28%;width:24%;height:9%"></div>
        <div class="aro" style="left:50%;top:42%;width:90%;height:21%"></div>
        <div class="aro" style="left:23%;top:90.5%;width:40%;height:13%"></div>
        <div class="aro" style="left:50%;top:90.5%;width:14%;height:13%"></div>
        <div class="aro" style="left:77%;top:90.5%;width:40%;height:13%"></div>
        <div class="punto" style="left:23%;top:79%">5</div>
        <div class="punto" style="left:50%;top:79%">6</div>
        <div class="punto" style="left:77%;top:79%">7</div>
      </div>
      <div class="punto izq" style="top:10%">1</div>
      <div class="punto der" style="top:9.5%">2</div>
      <div class="punto izq" style="top:28%">3</div>
      <div class="punto izq" style="top:42%">4</div>
    </div>
    <div style="flex:1">
      {refs([
        ("Nº de siniestro","El de RUS. Se puede copiar."),
        ("Hace cuánto no lo mirás","Gris está bien. Naranja: se está pasando."),
        ("Tercero o Asegurado","Los de tercero son los que más se escapan."),
        ("Los 3 pasos","Tocá el círculo para marcarlo: Informe, Cierre, Facturado."),
        ("Lo revisé","Tocalo cada vez que mirás el siniestro."),
        ("WhatsApp","Abre el chat con el teléfono cargado."),
        ("Abrir","Todos los datos, para verlos o corregirlos."),
      ], una=True)}
    </div>
  </div>

  <div class="nota ok"><b>Cuando cobrás uno, marcá "Facturado".</b> La tarjeta desaparece
  de la lista en el acto y queda guardada en Configuración. No se borra nunca.</div>

  <div class="nota"><b>La franja de color de la izquierda</b> te dice de un vistazo cómo viene:
  roja es urgente, naranja está por vencerse, verde está al día.</div>

  {pie(4)}
</section>

<!-- 5. ACTUALIZAR -->
<section class="hoja">
  <div class="cinta"><div class="num">4</div><div>
    <h2>Traer lo nuevo de RUS</h2>
    <p>Una vez por semana alcanza</p></div></div>

  <div class="pasos-grandes" style="gap:4mm;margin-bottom:6mm">
    <div class="paso-g" style="padding:5mm 7mm"><div class="bola" style="width:12mm;height:12mm;font-size:15pt">1</div><div>
      <h3 style="font-size:12.5pt">Bajá el archivo de RUS</h3>
      <p style="font-size:10.5pt">El <b>TareaAsignada.xls</b> de siempre.</p></div></div>
    <div class="paso-g" style="padding:5mm 7mm"><div class="bola" style="width:12mm;height:12mm;font-size:15pt">2</div><div>
      <h3 style="font-size:12.5pt">Tocá "Actualizar lista" y arrastrá el archivo</h3>
      <p style="font-size:10.5pt">O hacé clic en el recuadro para buscarlo.</p></div></div>
  </div>

  <div class="captura">
    <div class="foto"><img src="{img('importar')}">
      <div class="aro" style="left:14%;top:20.5%;width:25%;height:13%"></div>
      <div class="aro" style="left:38%;top:20.5%;width:24%;height:13%"></div>
      <div class="aro" style="left:87%;top:94.5%;width:22%;height:8%"></div>
      <div class="punto" style="left:14%;top:11%">3</div>
      <div class="punto" style="left:38%;top:11%">4</div>
    </div>
    <div class="punto der" style="top:94.5%">5</div>
  </div>

  {refs([
    ("Los que faltaban","Estos se van a agregar."),
    ("Los que ya estaban","Ésos NO se agregan de nuevo. Nunca se duplican."),
    ("Agregar","Tocá el botón azul y listo."),
  ], desde=3)}

  {pie(5)}
</section>

<!-- 6. LO DEMAS -->
<section class="hoja">
  <div class="cinta"><div class="num">5</div><div>
    <h2>Dos cosas más</h2>
    <p>Por las dudas</p></div></div>

  <div style="display:flex;gap:7mm;align-items:flex-start">
    <div style="flex:1">
      <h3 style="font-size:13pt;font-weight:750;margin-bottom:3mm">¿Marcaste algo facturado sin querer?</h3>
      <p style="font-size:10.5pt;color:#4a5a72;line-height:1.55;margin-bottom:4mm">
      Entrá al <b>engranaje</b> de arriba a la derecha y tocá
      <b>"Ver los facturados"</b>. Buscá el siniestro, destildá <b>Facturado</b>
      y vuelve solo a la lista.</p>
      <p style="font-size:10.5pt;color:#4a5a72;line-height:1.55">
      También lo encontrás escribiendo el número en el buscador: aparece
      aunque esté facturado.</p>
    </div>
    <div class="captura" style="width:88mm;flex:none;padding:0">
      <div class="foto"><img src="{img('config')}">
        <div class="aro" style="left:50%;top:40%;width:93%;height:6.5%"></div>
      </div>
    </div>
  </div>

  <div class="nota" style="margin-top:8mm"><b>Nada se borra.</b> Marcar algo como facturado
  sólo lo saca de la vista. Sigue guardado y se puede recuperar en cualquier momento.</div>

  <h3 style="font-size:13pt;font-weight:750;margin:8mm 0 3mm">Si algo no se entiende</h3>
  <p style="font-size:10.5pt;color:#4a5a72;line-height:1.55">
  Preguntale a Ivo. Nada de lo que toques puede romper el sistema: todo se
  puede volver atrás.</p>

  <div style="margin-top:11mm;border:1.5px solid #1e5eb8;border-radius:3mm;padding:7mm 8mm;background:#f4f8fd">
    <div style="font-size:9pt;font-weight:800;letter-spacing:.08em;color:#1e5eb8;
      text-transform:uppercase;margin-bottom:4mm">Para acordarse</div>
    <div style="display:flex;gap:6mm">
      <div style="flex:1">
        <div style="font-size:20pt;font-weight:800;color:#1e5eb8;line-height:1">1</div>
        <b style="font-size:11pt;display:block;margin:1.5mm 0 1mm">Tocá "Lo revisé"</b>
        <span style="font-size:9.5pt;color:#4a5a72;line-height:1.45">Cada vez que
        mirás un siniestro.</span>
      </div>
      <div style="flex:1">
        <div style="font-size:20pt;font-weight:800;color:#1e5eb8;line-height:1">2</div>
        <b style="font-size:11pt;display:block;margin:1.5mm 0 1mm">Marcá "Facturado"</b>
        <span style="font-size:9.5pt;color:#4a5a72;line-height:1.45">Cuando cobrás,
        para que salga de la lista.</span>
      </div>
      <div style="flex:1">
        <div style="font-size:20pt;font-weight:800;color:#1e5eb8;line-height:1">3</div>
        <b style="font-size:11pt;display:block;margin:1.5mm 0 1mm">Actualizá una vez por semana</b>
        <span style="font-size:9.5pt;color:#4a5a72;line-height:1.45">Con el archivo
        que bajás de RUS.</span>
      </div>
    </div>
  </div>

  {pie(6)}
</section>

</body></html>"""

open('manual.html','w',encoding='utf-8').write(html)
print('manual.html listo:', len(html)//1024, 'KB')
