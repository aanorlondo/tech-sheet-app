#!/bin/bash

# PSQL ADMIN DB
export POSTGRES_DB=psql-local
export POSTGRES_USER=admin
export POSTGRES_PASSWORD=admin

# PSQL APPDETAILS INFO
export PSQL_HOST=$(hostname)
export PSQL_PORT=5432
export PSQL_DBNAME=${POSTGRES_DB}
export PSQL_TABLE=app_details
export PSQL_USER=app-user
export PSQL_PSWD=appdetails
