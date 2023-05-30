-- Create the database if it doesnt exist
SELECT 'CREATE DATABASE ${PSQL_DBNAME}'
WHERE NOT EXISTS (
  SELECT FROM pg_database WHERE datname = '${PSQL_DBNAME}'
)\gexec

-- list all databases
\l

-- Connect to the database
\c ${PSQL_DBNAME};

-- Create a user if not exists
DO $$
BEGIN
  IF NOT EXISTS (
    SELECT FROM pg_catalog.pg_user WHERE usename = '${PSQL_USER}'
  ) THEN
    EXECUTE 'CREATE ROLE ${PSQL_USER} WITH LOGIN PASSWORD ' || quote_literal('${PSQL_PSWD}');
  END IF;
END$$;

-- Grant necessary privileges to the user
GRANT ALL PRIVILEGES ON DATABASE ${PSQL_DBNAME} TO ${PSQL_USER};

-- list all databases
\l

-- Create the app_details table if it doesnt exist
CREATE TABLE IF NOT EXISTS ${PSQL_TABLE} (
  app_id VARCHAR(255) PRIMARY KEY,
  url VARCHAR(255),
  name VARCHAR(255),
  description VARCHAR(255),
  frontend_technology VARCHAR(255),
  backend_technology VARCHAR(255),
  database_technology VARCHAR(255),
  author VARCHAR(255),
  github_url VARCHAR(255)
);

-- Grant necessary privileges to the user for the table
GRANT ALL PRIVILEGES ON TABLE ${PSQL_TABLE} TO ${PSQL_USER};

--- list all tables
\dt+

--- show details of table
\d+ ${PSQL_TABLE}