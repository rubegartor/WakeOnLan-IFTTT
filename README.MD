# IFTTT - Wake On LAN (Google Nest Mini)

Implementación de "Wake On LAN" con Google Nest Mini, IFTTT y Flask

### Creación del Applet en IFTTT
Para crear un Applet customizado: https://ifttt.com/create

**IF THIS:**

_1._ Se crea un enlace con Google Assistant

**THEN THAT:**

_1._ Se crea un webhook apuntando al servidor con el servidor Flask (El servidor deberá estar al mismo tiempo en la misma red que el pc)

_1.2._ Ejemplo:




### Generar certificados
Los certificados se generarán sobre la base del proyecto en la carpeta "Certs"
```
openssl req -x509 -newkey rsa:4096 -nodes -out Certs/cert.pem -keyout Certs/key.pem -days 365
```