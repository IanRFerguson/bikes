WITH
    chicago AS (
        SELECT

            *

        FROM {{ ref("stg__bikes") }}
        WHERE LOWER(city) = 'chicago'
    )

SELECT

    ROUND(longitude::NUMERIC, 2) AS rounded_longitude,
    ROUND(latitude::NUMERIC, 2) AS rounded_latitude,
    COUNT(*) AS existing_stations,
    SUM(free_bikes + empty_slots) AS bike_capacity
    SUM(free_bikes) AS total_free_bikes,
    SUM(empty_slots) AS total_empty_slots

FROM chicago
GROUP BY 1,2