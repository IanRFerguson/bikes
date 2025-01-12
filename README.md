# Bike Share Analytics

This code pulls data from the City Bikes API into a local Postgres instance using `dlt`, then performs some meaningful transformations using `dbt` to prepare an analytics team for their assessment of where new bike share stations should go.

## Setup

This pipeline is setup to run on your local machine or in Docker. Wherever you're running, you'll want to start with `make setup` to create the credential files required to execute the pipeline.

### Running Locally
The local pipeline run assumes that you're able to run a local Postgres database using Homebrew. For more information on setting that up, [read these docs](https://wiki.postgresql.org/wiki/Homebrew).

You'll want to configure a local database with the following information:
```
HOST:       localhost
DB:         analytics
PORT:       5432

USER:       bikes
PASSWORD:   dev
```

### Running with Docker
The pseudo-production version of this pipeline can be run with `make pipeline` - this requires the `local.env` file to be populated with database connection information (which is required in both the load and transform steps here).

