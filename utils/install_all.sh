### Actualizar paquetes de instalacion
sudo apt-get update

### Descargar archivo docker de repositorio e instalar docker
wget https://raw.githubusercontent.com/FabianRuizF/clase_big_data/main/utils/install_docker.sh
sudo bash install_docker.sh

### Instalar pip3 para poder ser usado
sudo apt-get install python3-pip -y

### Instalar version de pyspark especifica
pip3 install pyspark==3.0.2

### Instalar Java-jdk
apt-get install openjdk-8-jdk-headless -qq

### Unirse al docker-swarm
docker swarm join --token SWMTKN-1-01gwxz2v1ob8wdnq2zfasryodtaf54i9g291bbob41nwmu3h6v-2v3e59m691nmg43rlsi29q8bq 139.144.62.82:2377

### Descargar archivo de docker-compose y configurar con el nombre y apellido adecuado
wget https://raw.githubusercontent.com/FabianRuizF/clase_big_data/main/clase3/docker-compose.yml
sed -i 's/localhost/fabian-ruiz/g' /etc/hostname
sed -i 's/localhost/fabian-ruiz/g' /etc/hosts
sed -i 's/nombre/fabian/g' docker-compose.yml
sed -i 's/apellido/ruiz/g' docker-compose.yml

### Reiniciar para que los nombres tomen efecto
sudo reboot

