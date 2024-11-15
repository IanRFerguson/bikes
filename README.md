# Bike Share Analytics

This code pulls data from the City Bikes API into a local Postgres instance using `dlt`, then performs some meaningful transformations using `dbt`

```
# Using a local Postgres instance
make local

# Using Docker services
make dev
```