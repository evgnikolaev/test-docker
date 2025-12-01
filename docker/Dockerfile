FROM ubuntu:22.04
LABEL author=RomNero
LABEL platform=Youtube
RUN apt-get update
RUN apt-get install nginx -y
WORKDIR /var/www/html/
COPY files/index.html .
EXPOSE 80
EXPOSE 443/tcp
CMD ["nginx","-g", "daemon off;"]
