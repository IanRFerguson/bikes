import dlt
import os
from dlt.sources.rest_api import rest_api_source
from utilities.logger import logger

##########

POSTGRES_ENV_MAP = {
    "database": "DB",
    "username": "USER",
    "password": "PASSWORD",
    "host": "HOST",
    "port": "PORT",
}


def setup_credentials():
    """
    Loops through production environment variables
    and assigns them to the expected dlt.secret variable
    """

    # This is the base credential string that we'll append to
    secret_base = "citi_bike_prod.destination.postgres.credentials"

    for dlt_var, env_var in POSTGRES_ENV_MAP.items():
        # Attach expected variable to the credential string
        # based on the Postgres variables in the environment
        dlt_secret__key = f"{secret_base}.{dlt_var}"
        env_var__key = f"DBT_PG_{env_var}__PROD"

        dlt.secrets[dlt_secret__key] = os.environ[env_var__key]

        logger.debug(f"Setting {dlt_secret__key} with {env_var__key} ENV VAR")

    dlt.secrets[f"{secret_base}.connect_timeout"] = 90


if os.environ.get("PROD") == "true":
    PIPELINE_NAME = "citi_bike_prod"
    setup_credentials()
else:
    PIPELINE_NAME = "citi_bike_dev"


def load_citi_bike_data():
    logger.info("Running CityBike API load into Postgres...")

    pipeline = dlt.pipeline(
        pipeline_name=PIPELINE_NAME,
        destination="postgres",
        dataset_name="raw_citi_bike__nyc",
    )

    config = rest_api_source(
        {
            "client": {
                "base_url": "http://api.citybik.es/v2/",
            },
            "resource_defaults": {
                "write_disposition": "replace",
                "endpoint": {
                    "params": {
                        "limit": None,
                    },
                    "data_selector": "network[stations]",
                },
            },
            "resources": [
                "networks/bay-wheels",
                "networks/citi-bike-nyc",
                "networks/divvy",
            ],
        }
    )

    resp = pipeline.run(config)
    logger.info(resp)


#####

if __name__ == "__main__":
    load_citi_bike_data()
