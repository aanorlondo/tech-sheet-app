import os
from flask import Flask, request
from flask_cors import CORS
from psql_helper import (
    connect_to_db,
    generate_get_app_request,
    generate_update_app_request,
    generate_create_app_request,
    genenerate_count_entries_request,
    ID_FIELD,
    URL_FIELD,
    NAME_FIELD,
    DESC_FIELD,
    FRONT_FIELD,
    BACK_FIELD,
    DB_FIELD,
    AUTHOR_FIELD,
    GITHUB_FIELD,
)
from console_logger import logger

app = Flask(__name__)
CORS(app)


def make_response(status: str, message: str, data: dict | list = None) -> dict:
    """
    Default response body structure template
    """
    return {
        "status": status,
        "message": message,
        "data": data,
    }


# GET /
@app.route("/", methods=["GET"])
def get_app_details():
    """
    Get the details of an app with the given ID.
    Args:
        app_id (str): ID of the app. Given as query param
    Returns:
        dict: Dictionary containing the details of the app. If the app does not exist, returns None.
    """
    app_id = request.args.get("app_id")

    if not app_id:
        message = "Missing 'app_id' parameter."
        logger.info(message)
        return make_response(status="fail", message=message), 400

    logger.info(f"Received GET/app-details for ID: {app_id}...")
    try:
        logger.info((f"Connecting to DB..."))
        conn = connect_to_db()
        cur = conn.cursor()
        logger.info("Getting App details...")
        cur.execute(generate_get_app_request(app_id))
        app = cur.fetchone()
        cur.close()
        conn.close()

        if app:
            app_details = {
                URL_FIELD: app[0],
                NAME_FIELD: app[1],
                DESC_FIELD: app[2],
                FRONT_FIELD: app[3],
                BACK_FIELD: app[4],
                DB_FIELD: app[5],
                AUTHOR_FIELD: app[6],
                GITHUB_FIELD: app[7],
            }
            message = "App details succesfully fetched"
            logger.info(f"{message}: {app_details}")
            return (
                make_response(status="success", message=message, data=app_details),
                200,
            )
        else:
            message = "App details not found."
            logger.info(message)
            return (make_response(status="fail", message=message), 404)
    except Exception as e:
        message = f"ERROR on GET <app_id> operation: {e}"
        logger.error(message)
        return (make_response(status="fail", message=message), 500)


# POST /{body}
@app.route("/", methods=["POST"])
def update_app_details():
    """
    Set or update the details of an app with the given ID.
    Args:
        body (dict): App details to be updated or created, including the app_id. Given as request json.
    Returns:
        dict: Dictionary indicating the success or failure of the operation.
    """
    body = request.json

    if not body:
        message = "Missing request body."
        logger.error(message)
        return make_response(status="fail", message=message), 400

    logger.info(f"Received POST/body={body}")
    app_id = body.get(ID_FIELD)
    if not app_id:
        message = "Missing app_id in the request body."
        logger.error(message)
        return make_response(status="fail", message=message), 400

    try:
        logger.info(f"Checking Apps with ID={app_id}...")
        count_query = genenerate_count_entries_request(app_id)
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(count_query)
        result = cur.fetchone()
        entry_count = result[0]

        if entry_count == 0:
            logger.info(f"App {app_id} does not exist, creating one...")
            cur.execute(
                generate_create_app_request(
                    app_id,
                    body[URL_FIELD],
                    body[NAME_FIELD],
                    body[DESC_FIELD],
                    body[FRONT_FIELD],
                    body[BACK_FIELD],
                    body[DB_FIELD],
                    body[AUTHOR_FIELD],
                    body[GITHUB_FIELD],
                )
            )
        else:
            logger.info(f"App {app_id} already exists. Updating...")
            cur.execute(
                generate_update_app_request(
                    app_id,
                    body[URL_FIELD],
                    body[NAME_FIELD],
                    body[DESC_FIELD],
                    body[FRONT_FIELD],
                    body[BACK_FIELD],
                    body[DB_FIELD],
                    body[AUTHOR_FIELD],
                    body[GITHUB_FIELD],
                )
            )
        conn.commit()
        cur.close()
        conn.close()
        message = "App details successfully updated!"
        logger.info(message)
        return (make_response(status="success", message=message), 200)
    except Exception as e:
        message = f"ERROR on update/create app details entry: {e}"
        logger.error(message)
        return (make_response(status="fail", message=message), 500)
