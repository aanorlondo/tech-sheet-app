FROM python:3.10-alpine

WORKDIR /flask-app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./app/ ./app

ENV PSQL_HOST=${PSQL_HOST}
ENV PSQL_PORT=${PSQL_PORT}
ENV PSQL_DBNAME=${PSQL_DBNAME}
ENV PSQL_TABLE=${PSQL_TABLE}
ENV PSQL_USER=${PSQL_USER}
ENV PSQL_PSWD=${PSQL_PSWD}

WORKDIR /flask-app/app

EXPOSE 3500
CMD ["flask", "run", "--host=0.0.0.0", "--port=3500"]