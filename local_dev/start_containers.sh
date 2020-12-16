#!/bin/bash

docker volume create dev.influxdb

docker run -p 8086:8086 \
  -v dev.influxdb:/var/lib/influxdb \
  --name dev.influxdb \
  -d \
  influxdb

curl -G http://localhost:8086/query --data-urlencode "q=CREATE DATABASE weather"
