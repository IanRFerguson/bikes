{{
    config(
        cluster_by=["city"],
        tags=["production"]
    )
}}

SELECT

    *

FROM {{ ref("stg__bikes") }}