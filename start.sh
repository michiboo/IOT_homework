#!/bin/bash


sudo docker run -it -d -p 1883:1883 -p 9001:9001  --mount type=bind,source=$PWD/mosquitto.conf,target=/mosquitto/config/mosquitto.conf eclipse-mosquitto 


cd ./nodeRed && sudo docker build -t nodered .
sudo docker run -d -p 1880:1880 -v node_red_data:/data --name mynodered -t nodered
sudo docker exec mynodered bash -c "cd /usr/src/node-red;npm install node-red-contrib-influxdb  &&  npm install node-red-dashboard" 
sudo docker run -p 8086:8086 \
      -v $PWD:/var/lib/influxdb2 \
      influxdb:2.0 