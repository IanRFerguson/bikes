from utilities.dbt_helpers import run_dbt_pipeline
from utilities.rest_api_pipeline import load_citi_bike_data

if __name__ == "__main__":
    load_citi_bike_data()
    run_dbt_pipeline()
