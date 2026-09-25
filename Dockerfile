# Imagen de la pieza sitio-portafolio: nginx sirviendo el index.html.
FROM nginx:alpine
COPY pieza/ /usr/share/nginx/html/
EXPOSE 80
