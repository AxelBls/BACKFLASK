## LANCEMENT MANUEL POUR LE BACK

### Pour lancer l'application de base de données (MYSQL)

```shell
docker run -d --name dbm -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 \
-v /var/log/mysql-db:/var/log/mysql astondevops/docker-mysql-5.6

#Il est nécessaire de se mettre en venv
```
### CONFIGURATION DE LA BDD SOUS PyCharm

- Configurer une nouvelle datasource MySQL
- l'hôte est l'ip du serveur
- le login est root
- le mot de passe est password
- Ensuite, il faut créer le schema ProjetFilRouge
- Executer le fichier *ProjetFilRouge.sql*

### Pour lancer l'application phpMyAdmin

```shell
#Il faut toujours être en venv
docker run -d  --name phpmyadmin --link dbm:mysql \
 -e MYSQL_USERNAME=root -p 8181:80 nazarpc/phpmyadmin 
```

- lancer le navigateur à l'adresse <ip>:8181
- Login : root | Mot de passe : password

### Pour lancer l'application flask :
```shell
docker build -t pfr-mysql .
docker run -d -it --name mypfr --link dbm:pfr -p 5000:5000 pfr-mysql
```

## LANCEMENT AUTOMATIQUE VIA DOCKER-COMPOSE
```shell
docker-compose up -d --build
```
## POUR STOPPER TOUT LES CONTENEURS
```shell
docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)
```



sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install docker
pip3 install docker-compose