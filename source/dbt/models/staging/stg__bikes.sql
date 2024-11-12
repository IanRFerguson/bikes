-- NOTE: This could be refactored with dbt utils
WITH
    chicago AS (
        SELECT 

            id,
            name,
            latitude,
            longitude,
            timestamp,
            free_bikes,
            empty_slots,
            'networks_divvy' AS source_table,
            'Chicago' AS city

        FROM {{ source("raw_bikes", "networks_divvy")}}
    ),

    new_york AS (
        SELECT 

            id,
            name,
            latitude,
            longitude,
            timestamp,
            free_bikes,
            empty_slots,
            'networks_citi_bike_nyc' AS source_table,
            'New York' AS city

        FROM {{ source("raw_bikes", "networks_citi_bike_nyc")}}
    ),

    san_francisco AS (
        SELECT 

            id,
            name,
            latitude,
            longitude,
            timestamp,
            free_bikes,
            empty_slots,
            'networks_bay_wheels' AS source_table,
            'San Francisco' AS city

        FROM {{ source("raw_bikes", "networks_bay_wheels")}}
    ),

    stack AS (
        SELECT * FROM chicago
        UNION ALL
        SELECT * FROM new_york
        UNION ALL
        SELECT * FROM san_francisco
    )

SELECT

    *,
    CURRENT_TIMESTAMP AS _transform_timestamp

FROM stack