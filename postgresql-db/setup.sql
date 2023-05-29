-- Create a user if not exists
IF NOT EXISTS (
  SELECT FROM pg_catalog.pg_user WHERE usename = app-user
) THEN
  CREATE ROLE app-user WITH LOGIN PASSWORD appdetails;
END IF;


-- Grant necessary privileges to the user
GRANT ALL PRIVILEGES ON DATABASE psql-local TO app-user;

-- Create the app_details table if it doesnt exist
CREATE TABLE IF NOT EXISTS app_details (
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
