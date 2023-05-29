#!/bin/bash

source prepare_env.sh
source prepare_db_setup.sh

docker rmi -f negan/appdetails_psql:local
docker build -t negan/appdetails_psql:local ../postgresql-db
docker push negan/appdetails_psql:local

docker rm -f APPDETAILS-PSQL-LOCAL
docker run \
    -d \
    -e POSTGRES_DB=${POSTGRES_DB} \
    -e POSTGRES_USER=${POSTGRES_USER} \
    -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
    -e PSQL_DBNAME=${PSQL_DBNAME} \
    -e PSQL_TABLE=${PSQL_TABLE} \
    -e PSQL_USER=${PSQL_USER} \
    -e PSQL_PSWD=${PSQL_PSWD} \
    -p 5432:5432 \
    --name APPDETAILS-PSQL-LOCAL \
    negan/appdetails_psql:local
