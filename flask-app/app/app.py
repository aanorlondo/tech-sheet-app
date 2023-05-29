from flask import Flask
from flask_restful import Api, Resource
from flask_restful_swagger import swagger
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
api = swagger.docs(Api(app), apiVersion="1.0", api_spec_url="/api/spec.yaml")


class AppDetailsResource(Resource):
    # / GET (app_id)
    @swagger.operation(
        notes="Get app details by ID",
        parameters=[
            {
                "name": f"{ID_FIELD}",
                "description": "ID of the app",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "path",
            }
        ],
        responseClass=dict.__name__,
        responseMessages=[{"code": 200, "message": "OK"}],
    )
    def get(self, app_id):
        """
        Get the details of an app with the given ID.
        Args:
            app_id (str): ID of the app.
        Returns:
            dict: Dictionary containing the details of the app. If the app does not exist, returns None.
        """
        logger.info(f"Received GET/app-details for ID: {app_id}...")
        try:
            logger.info((f"Connecting to DB..."))
            conn = connect_to_db()
            cur = conn.cursor()
            logger.info("Execute SELECT request...")
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
                logger.info(f"App details succesfully fetched: {app_details}")
                return app_details
            else:
                logger.info(f"App details not found.")
                return {"message": "App details not found"}, 404
        except Exception as e:
            logger.error(f"ERROR on GET operation: {e}")
            return {"message": str(e)}, 500

    # / POST (body)
    @swagger.operation(
        notes="Update or create app details by ID",
        parameters=[
            {
                "name": "body",
                "description": "App details to be updated or created",
                "required": True,
                "allowMultiple": False,
                "dataType": "AppDetailsRequest",
                "paramType": "body",
            },
        ],
        responseClass=dict.__name__,
        responseMessages=[{"code": 200, "message": "OK"}],
    )
    def post(self, body):
        """
        Set or update the details of an app with the given ID.
        Args:
            body (dict): App details to be updated or created, including the app_id.
        Returns:
            dict: Dictionary indicating the success or failure of the operation.
        """
        logger.info(f"Received POST/body={body}")

        app_id = body.get("app_id")
        if not app_id:
            error_message = "Missing app_id in the request body."
            logger.error(f"ERROR: {error_message}")
            return {"message": error_message}, 400

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

            logger.info(f"App details successfully updated !")
            cur.close()
            conn.close()
            return body
        except Exception as e:
            logger.error(f"ERROR on update/create app details entry: {e}")
            return {"message": str(e)}, 500


api.add_resource(AppDetailsResource, "/app-details/<app_id>")
