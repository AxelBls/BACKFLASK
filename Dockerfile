#Ce fichier nous permet de réaliser les différentes taches utiles au lancement de notre application flask
#Entre autre : les installations de dépendance , la mise à jour des paquets, l'installation des paquets
#indiqués dans le requirements.txt ainsi que le lancement du serveur flask

FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3 python3-pip vim iputils-ping python3-mysqldb
RUN pip3 install pymysql cryptography
ADD templates /opt/templates
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY back.py /opt
COPY back.cfg /opt

ENTRYPOINT FLASK_APP=/opt/back.py flask run --host=0.0.0.0
