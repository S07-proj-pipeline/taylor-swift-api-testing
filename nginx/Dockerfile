FROM nginx:alpine

# Remove os ficheiros padrão do Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia a página inicial criada
COPY index.html /usr/share/nginx/html/

EXPOSE 80