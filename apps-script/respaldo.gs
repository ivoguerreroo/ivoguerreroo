/**
 * Servicio de respaldo por mail — Radar de Siniestros
 * ---------------------------------------------------
 * Recibe el respaldo desde la página y lo manda por mail como adjunto .json.
 * Se publica como "aplicación web" de Google Apps Script: es gratis, no
 * necesita dominio propio ni tarjeta, y el mail sale de tu propia cuenta.
 *
 * CÓMO PUBLICARLO (una sola vez):
 *   1. Entrá a https://script.google.com  ->  Nuevo proyecto
 *   2. Borrá lo que haya y pegá TODO este archivo
 *   3. Cambiá las dos constantes de abajo (DESTINO y CLAVE)
 *   4. Implementar  ->  Nueva implementación  ->  tipo "Aplicación web"
 *        Ejecutar como:      Yo
 *        Quién tiene acceso: Cualquier usuario
 *   5. Autorizá los permisos cuando los pida (es tu propia cuenta)
 *   6. Copiá la URL que termina en /exec y pegala en la página,
 *      en Configuración -> Respaldo automático
 */

// A dónde se manda el respaldo. Está fijo acá a propósito: aunque alguien
// descubra la URL, no puede usar el servicio para mandar mails a otro lado.
var DESTINO = 'walterguerreroseguros@gmail.com';

// Cambiala por cualquier frase inventada. Tiene que ser la misma que cargues
// en la página. Evita que un desconocido use la URL para mandarte mails.
var CLAVE = 'siniestro-peritaje-uruguay-rio-8037';

function doPost(e) {
  try {
    if (!e || !e.postData || !e.postData.contents) {
      return responder({ ok: false, error: 'Llegó un pedido vacío' });
    }
    var datos = JSON.parse(e.postData.contents);

    if (String(datos.clave || '') !== CLAVE) {
      return responder({ ok: false, error: 'Clave incorrecta' });
    }
    if (!datos.contenido) {
      return responder({ ok: false, error: 'El respaldo vino vacío' });
    }

    var nombre = datos.nombre || 'respaldo-siniestros.json';
    var adjunto = Utilities.newBlob(datos.contenido, 'application/json', nombre);

    MailApp.sendEmail({
      to: DESTINO,
      subject: 'Respaldo de siniestros — ' + (datos.fecha || new Date().toLocaleDateString('es-AR')),
      body: [
        'Respaldo automático del Radar de Siniestros.',
        '',
        datos.resumen || '',
        '',
        'Guardá este mail. Si alguna vez se pierden los datos de la página,',
        'se recuperan con el archivo adjunto desde:',
        'Exportar -> Restaurar desde un respaldo.',
        '',
        'No hace falta contestar este mail.'
      ].join('\n'),
      attachments: [adjunto],
      name: 'Radar de Siniestros'
    });

    return responder({ ok: true, enviadoA: DESTINO });
  } catch (err) {
    return responder({ ok: false, error: String(err) });
  }
}

/** Sirve para probar en el navegador que la URL quedó bien publicada. */
function doGet() {
  return responder({ ok: true, mensaje: 'El servicio de respaldo está andando.' });
}

function responder(objeto) {
  return ContentService
    .createTextOutput(JSON.stringify(objeto))
    .setMimeType(ContentService.MimeType.JSON);
}
