#!/bin/bash

# PSQL ADMIN DB
export POSTGRES_DB=psql_admin
export POSTGRES_USER=admin
export POSTGRES_PASSWORD=admin

# PSQL APPDETAILS INFO
export PSQL_HOST="172.17.0.1" #host.docker.internal #$(hostname)
export PSQL_PORT=5432
export PSQL_DBNAME=psql_dev
export PSQL_TABLE=app_details
export PSQL_USER=app_user
export PSQL_PSWD=appdetails

# SWAGGER
export HOSTNAME=$(hostname)
input_swagger_file="../flask-app/app/api/api_template.json"
output_swagger_file="../flask-app/app/api/api.json"
envsubst < $input_swagger_file > $output_swagger_file

# AUTH SERVER
export AUTH_HOST=$(hostname)
export AUTH_SERVER="https://${AUTH_HOST}/go-auth"