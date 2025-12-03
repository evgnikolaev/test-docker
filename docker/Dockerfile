FROM ubuntu:22.04
LABEL author=RomNero
LABEL platform=Youtube
RUN apt-get update
RUN apt-get install nginx -y
WORKDIR /var/www/html/

COPY files/index.html .
COPY files/script.sh /opt/script.sh
RUN chmod +x /opt/script.sh

ENV OWNER=RomNero
ENV TYPE=Demo
#  RUN echo $OWNER > /opt/info        - тут будет использована переменная задананая в Dockerfile
#  docker run -e OWNER=Billi "id"     - не отсюда

EXPOSE 80
EXPOSE 443/tcp

CMD ["/opt/script.sh"]
# CMD ["nginx","-g", "daemon off;"]  эту перенесли в script.sh