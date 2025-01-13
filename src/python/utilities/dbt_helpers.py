import os
import subprocess

from utilities.logger import logger
from utilities.setup_credentials import setup_credentials

##########

STAGE = "prod" if os.environ.get("PROD") == "true" else "dev"


def get_dbt_directory():
    """
    Infer runtime directory for local vs. containerized runs
    """

    if STAGE == "prod":
        _dbt_project_path = "/app/src/dbt"
    else:
        _current_directory_path = os.path.dirname(os.path.realpath(__file__))
        _dbt_project_path = os.path.abspath(
            os.path.join(_current_directory_path, "../..", "dbt")
        )

    logger.info(f"Running dbt in {_dbt_project_path}...")

    return _dbt_project_path


def run_dbt_pipeline():
    _dbt_project_path = get_dbt_directory()

    # Change working directory to dbt submodule
    # NOTE - Find a more ephemeral way to do this
    os.chdir(_dbt_project_path)

    # Run dbt as subprocess
    command = "dbt build -s +path:models/production"

    if STAGE == "prod":
        command += " -t prod"
        setup_credentials(source="dbt")

    _run_status = subprocess.run(command, shell=True)

    if _run_status.returncode != 0:
        logger.error("FAILED TO RUN dbt")
        raise RuntimeError(_run_status.returncode)

    logger.info("Succesfully rebuilt production tables")
