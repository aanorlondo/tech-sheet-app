#!/bin/bash

source prepare_env.sh

docker rmi -f negan/appdetails_api:local
docker build -t negan/appdetails_api:local ../flask-app
docker push negan/appdetails_api:local


docker rm -f APPDETAILS-API-LOCAL
docker run \
    -d \
    -e PSQL_HOST=${PSQL_HOST} \
    -e PSQL_PORT=${PSQL_PORT} \
    -e PSQL_DBNAME=${PSQL_DBNAME} \
    -e PSQL_TABLE=${PSQL_TABLE} \
    -e PSQL_USER=${PSQL_USER} \
    -e PSQL_PSWD=${PSQL_PSWD} \
    -p 3500:3500 \
    --name APPDETAILS-API-LOCAL \
    negan/appdetails_api:local