import dlt
import os
from dlt.sources.rest_api import rest_api_source
from utilities.setup_credentials import setup_credentials
from utilities.logger import logger

##########


if os.environ.get("PROD") == "true":
    PIPELINE_NAME = "citi_bike_prod"
    setup_credentials(source="dlt")
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
