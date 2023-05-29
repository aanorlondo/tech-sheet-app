#!/bin/bash

# Read the setup_with_vars.sql file
input_sql_file="../postgresql-db/setup_with_vars.sql"
output_sql_file="../postgresql-db/setup.sql"
sql_content=$(cat "$input_sql_file")

# Replace the environment variable placeholders with their values
eval "echo \"$sql_content\"" | envsubst > "$output_sql_file"
