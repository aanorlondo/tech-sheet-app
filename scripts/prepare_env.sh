#!/bin/bash

# PSQL ADMIN DB
export POSTGRES_DB=psql_admin
export POSTGRES_USER=admin
export POSTGRES_PASSWORD=admin

# PSQL APPDETAILS INFO
export PSQL_HOST=$(hostname)
export PSQL_PORT=5432
export PSQL_DBNAME=psql_dev
export PSQL_TABLE=app_details
export PSQL_USER=app_user
export PSQL_PSWD=appdetails

# AUTH SERVER
export AUTH_HOST=$(hostname)
export AUTH_SERVER="https://${AUTH_HOST}/go-auth"