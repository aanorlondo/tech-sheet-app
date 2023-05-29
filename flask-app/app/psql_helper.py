import os
import psycopg2


# ---------------- #
# CONNECTION TO DB #
# ---------------- #
def get_psql_host() -> str | None:
    return os.environ.get("PSQL_HOST", None)


def get_psql_port() -> int | None:
    return os.environ.get("PSQL_PORT", None)


def get_psql_dbname() -> str | None:
    return os.environ.get("PSQL_DBNAME", None)


def get_psql_table_name() -> str | None:
    return os.environ.get("PSQL_TABLE", None)


def get_psql_user() -> str | None:
    return os.environ.get("PSQL_USER", None)


def get_psql_pswd() -> str | None:
    return os.environ.get("PSQL_PSWD", None)


def connect_to_db():
    """
    Establishes a connection to the PostgreSQL database.
    Returns:
        Connection object representing the database connection.
    """
    return psycopg2.connect(
        host=get_psql_host(),
        port=get_psql_port(),
        dbname=get_psql_dbname(),
        user=get_psql_user(),
        password=get_psql_pswd(),
    )


# ---------- #
# SETUP KEYS #
# ---------- #

ID_FIELD = "app_id"
URL_FIELD = "url"
NAME_FIELD = "name"
DESC_FIELD = "description"
FRONT_FIELD = "front_technology"
BACK_FIELD = "backend_technology"
DB_FIELD = "database_technology"
AUTHOR_FIELD = "author"
GITHUB_FIELD = "github_url"


# --------------- #
# CRUD OPERATIONS #
# --------------- #


# // CREATE (INSERT)
def generate_create_app_request(
    app_id: str,
    url: str,
    name: str,
    description: str,
    frontend_technology: str,
    backend_technology: str,
    databaase_technology: str,
    author: str,
    github_url: str,
) -> str:
    """
    Generate SQL query to create a new app entry.
    Args:
        app_id (str): ID of the app.
        url (str): URL of the app.
        name (str): Name of the app.
        description (str): Description of the app.
        frontend_technology (str): Front-end technology of the app.
        backend_technology (str): Back-end technology of the app.
        databaase_technology (str): Database technology of the app.
        author (str): Author of the app.
        github_url (str): GitHub URL of the app.
    Returns:
        str: SQL query to create a new app entry.
    """

    return f"""
    INSERT INTO {get_psql_table_name()} (
        {ID_FIELD},
        {URL_FIELD},
        {NAME_FIELD},
        {DESC_FIELD},
        {FRONT_FIELD},
        {BACK_FIELD},
        {DB_FIELD},
        {AUTHOR_FIELD},
        {GITHUB_FIELD}
    )
    VALUES (
        {app_id},
        {url},
        {name},
        {description},
        {frontend_technology},
        {backend_technology},
        {databaase_technology},
        {author},
        {github_url}
    )
    """


# // READ (SELECT)
def generate_get_app_request(app_id: str) -> str:
    """
    Generate SQL query to retrieve app details by ID.
    Args:
        app_id (str): ID of the app.
    Returns:
        str: SQL query to retrieve app details.
    """

    return f"""
    SELECT 
        {URL_FIELD},
        {NAME_FIELD},
        {DESC_FIELD},
        {FRONT_FIELD},
        {BACK_FIELD},
        {DB_FIELD},
        {AUTHOR_FIELD},
        {GITHUB_FIELD}
    FROM
        {get_psql_table_name()}
    WHERE
        {ID_FIELD} = {app_id};
    """


# // READ (COUNT)
def genenerate_count_entries_request(app_id: str) -> str:
    """
    Generate a SQL query to count the number of entries with the given app_id.
    Args:
        app_id (str): ID of the app.
    Returns:
        str: SQL query to count the entries.
    """

    return f"""
    SELECT COUNT(*)
    FROM
        {get_psql_table_name()}
    WHERE
        {ID_FIELD} = {app_id}
    """


# // UPDATE
def generate_update_app_request(
    app_id: str,
    url: str,
    name: str,
    description: str,
    frontend_technology: str,
    backend_technology: str,
    databaase_technology: str,
    author: str,
    github_url: str,
) -> str:
    """
    Generate SQL query to update app details by ID.
    Args:
        app_id (str): ID of the app.
        url (str): URL of the app.
        name (str): Name of the app.
        description (str): Description of the app.
        frontend_technology (str): Front-end technology of the app.
        backend_technology (str): Back-end technology of the app.
        databaase_technology (str): Database technology of the app.
        author (str): Author of the app.
        github_url (str): GitHub URL of the app.
    Returns:
        str: SQL query to update app details.
    """

    return f"""
    UPDATE {get_psql_table_name()}
    SET
        {URL_FIELD} = {url},
        {NAME_FIELD} = {name},
        {DESC_FIELD} = {description},
        {FRONT_FIELD} = {frontend_technology},
        {BACK_FIELD} = {backend_technology},
        {DB_FIELD} = {databaase_technology},
        {AUTHOR_FIELD} = {author}, 
        {GITHUB_FIELD} = {github_url}
    WHERE
        {ID_FIELD} = {app_id}
    """
