#!/bin/bash
#
# Start up services that backend needs running
# This includes influxdb, redis?, 

if [[ ! -f backend/env ]]
then
  echo 'No backend/env file present, see backend/env.example'
  exit 1
fi

docker volume create dev.influxdb
docker stop dev.influxdb
docker rm dev.influxdb

docker run -p 8086:8086 \
  -v dev.influxdb:/var/lib/influxdb \
  --name dev.influxdb \
  -e INFLUXDB_ADMIN_USER=influxdb_user \
  -e INFLUXDB_ADMIN_PASSWORD=influxdb_pass \
  -e INFLUXDB_DB=influxdb_database \
  -d influxdb
