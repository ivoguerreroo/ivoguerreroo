var DESTINO = 'walterguerreroseguros@gmail.com';
var CLAVE = 'siniestro-peritaje-uruguay-rio-8037';

function doPost(e) {
  try {
    var datos = JSON.parse(e.postData.contents);
    if (String(datos.clave || '') !== CLAVE) {
      return responder({ ok: false, error: 'Clave incorrecta' });
    }
    if (!datos.contenido) {
      return responder({ ok: false, error: 'El respaldo vino vacio' });
    }
    var adjunto = Utilities.newBlob(datos.contenido, 'application/json',
                                    datos.nombre || 'respaldo-siniestros.json');
    MailApp.sendEmail({
      to: DESTINO,
      subject: 'Respaldo de siniestros - ' + (datos.fecha || ''),
      body: 'Respaldo automatico del Radar de Siniestros.\n\n' +
            (datos.resumen || '') + '\n\n' +
            'Guarda este mail. Si alguna vez se pierden los datos de la pagina, ' +
            'se recuperan con el archivo adjunto desde Exportar / Restaurar.',
      attachments: [adjunto],
      name: 'Radar de Siniestros'
    });
    return responder({ ok: true, enviadoA: DESTINO });
  } catch (err) {
    return responder({ ok: false, error: String(err) });
  }
}

function doGet() {
  return responder({ ok: true, mensaje: 'El servicio de respaldo esta andando.' });
}

function responder(objeto) {
  return ContentService.createTextOutput(JSON.stringify(objeto))
    .setMimeType(ContentService.MimeType.JSON);
}
