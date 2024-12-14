import os
import subprocess

from utilities.logger import logger

#####


def get_dbt_directory(stage: str):
    """
    Infer runtime directory for local vs. containerized runs
    """

    if stage.lower() == "prod":
        _dbt_project_path = "/app/source/dbt"
    else:
        _current_directory_path = os.path.dirname(os.path.realpath(__file__))
        _dbt_project_path = os.path.abspath(
            os.path.join(_current_directory_path, "../..", "dbt")
        )

    logger.info(f"Running dbt in {_dbt_project_path}...")
    return _dbt_project_path


def run_dbt_pipeline():
    # Use environment variables to infer where we're running dbt
    stage = os.environ.get("STAGE", "dev")
    _dbt_project_path = get_dbt_directory(stage=stage)

    # Change working directory to dbt submodule
    # NOTE - Find a more ephemeral way to do this
    os.chdir(_dbt_project_path)

    # Run dbt as subprocess
    command = "dbt build -s +path:models/production"

    if stage == "prod":
        command += " -t prod"

    # TODO - Raise exceptions
    _ = subprocess.run(command, shell=True)

    logger.info("Succesfully rebuilt production tables")
