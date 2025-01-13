import os
import dlt
from utilities.logger import logger

##########

DLT_POSTGRES_ENV_MAP = {
    "database": "DB",
    "username": "USER",
    "password": "PASSWORD",
    "host": "HOST",
    "port": "PORT",
}

DLT_PIPELINE_SECRET = "citi_bike_prod.destination.postgres.credentials"


def setup_credentials(source: str):
    if source == "dlt":
        _setup_dlt_credentials()

    elif source == "dbt":
        _setup_dbt_credentials()

    else:
        raise ValueError(
            f"Invalid `source` variable - {source}. Must be dbt or dlt`"
        )  # noqa


def _setup_dlt_credentials():
    """
    Load ENV variables in the format
    that dlt expects in the runtime environment
    """

    for dlt_format, env_var in DLT_POSTGRES_ENV_MAP.items():
        dlt_key = f"{DLT_PIPELINE_SECRET}.{dlt_format}"
        env_key = f"PG_{env_var}__PROD"

        dlt.secrets[dlt_key] = os.environ[env_key]
        logger.debug(f"Set {dlt_key} = {env_key}")

    dlt.secrets[f"{DLT_PIPELINE_SECRET}.connect_timeout"] = 90


def _setup_dbt_credentials():
    """
    Load ENV variables in the format
    that dbt expects in the runtime environment
    """

    for env_var in DLT_POSTGRES_ENV_MAP.values():
        dbt_key = f"DBT_PG_{env_var}__PROD"
        env_key = f"PG_{env_var}__PROD"

        os.environ[dbt_key] = os.environ[env_key]
        logger.debug(f"Set {dbt_key} = {env_key}")
