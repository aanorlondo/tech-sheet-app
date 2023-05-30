-- Create the database if it doesnt exist
SELECT 'CREATE DATABASE psql_dev'
WHERE NOT EXISTS (
  SELECT FROM pg_database WHERE datname = 'psql_dev'
)\gexec

-- list all databases
\l

-- Connect to the database
\c psql_dev;

-- Create a user if not exists
DO $$
BEGIN
  IF NOT EXISTS (
    SELECT FROM pg_catalog.pg_user WHERE usename = 'app_user'
  ) THEN
    EXECUTE 'CREATE ROLE app_user WITH LOGIN PASSWORD ' || quote_literal('appdetails');
  END IF;
END$$;

-- Grant necessary privileges to the user
GRANT ALL PRIVILEGES ON DATABASE psql_dev TO app_user;

-- list all databases
\l

-- Create the app_details table if it doesnt exist
CREATE TABLE IF NOT EXISTS app_details (
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
GRANT ALL PRIVILEGES ON TABLE app_details TO app_user;

--- list all tables
\dt+

--- show details of table
\d+ app_details