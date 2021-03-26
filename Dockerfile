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
