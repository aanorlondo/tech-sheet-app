#!/bin/bash

source prepare_env.sh
docker build -t negan/appdetails_api:rasp4 ../flask-app
docker push negan/appdetails_api:rasp4

host_ip=$(hostname -I | awk '{print $1}')
hostname=$(hostname)

docker rm -f APPDETAILS-API-LOCAL
docker run \
    -d \
    -e PSQL_HOST=${PSQL_HOST} \
    -e PSQL_PORT=${PSQL_PORT} \
    -e PSQL_DBNAME=${PSQL_DBNAME} \
    -e PSQL_TABLE=${PSQL_TABLE} \
    -e PSQL_USER=${PSQL_USER} \
    -e PSQL_PSWD=${PSQL_PSWD} \
    -e AUTH_SERVER=${AUTH_SERVER} \
    -p 3500:3500 \
    --add-host="host:${host_ip}" \
    --add-host="${hostname}:${host_ip}" \
    --name APPDETAILS-API-LOCAL \
    negan/appdetails_api:rasp4
