# Guía rápida (PDF)

`Guia-Radar-de-Siniestros.pdf` (en la raíz) es el manual de 6 páginas para
Walter. Está pensado para leerse en cinco minutos: casi todo son capturas
reales del sistema con números y aros señalando dónde tocar.

## Cómo se regenera

Las capturas de `capturas/` salen del sistema andando con los datos reales, y
el PDF se arma desde HTML con Chromium:

```bash
python3 generar-guia.py     # arma manual.html con las capturas embebidas
# después, con Playwright: page.pdf({format:'A4', printBackground:true})
```

Si cambia la interfaz hay que **volver a sacar las capturas**, porque los aros
y los números están posicionados en porcentajes sobre cada imagen: si se mueve
un botón, la marca queda en el lugar equivocado. Conviene revisar las 6 páginas
una por una después de regenerar.
