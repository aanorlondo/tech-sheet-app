-- Create the database if it doesnt exist
CREATE DATABASE IF NOT EXISTS ${PSQL_DBNAME};

-- Connect to the database
\c ${PSQL_DBNAME};

-- Create a user if not exists
DO $$BEGIN
  IF NOT EXISTS (
    SELECT FROM pg_catalog.pg_user WHERE usename = ${PSQL_USER}
  ) THEN
    CREATE ROLE ${PSQL_USER} WITH LOGIN PASSWORD ${PSQL_PSWD};
  END IF;
END$$;

-- Grant necessary privileges to the user
GRANT ALL PRIVILEGES ON DATABASE ${PSQL_DBNAME} TO ${PSQL_USER};

-- Create the app_details table if it doesnt exist
CREATE TABLE IF NOT EXISTS ${PSQL_TABLE} (
  app_id VARCHAR(255) PRIMARY KEY,
  url VARCHAR(255),
  name VARCHAR(255),
  description VARCHAR(255),
  front_technology VARCHAR(255),
  back_technology VARCHAR(255),
  database_technology VARCHAR(255),
  author VARCHAR(255),
  github_url VARCHAR(255)
);