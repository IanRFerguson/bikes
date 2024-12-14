#!/bin/bash

set -e

su postgres -c "pg_ctl start -l /var/lib/postgresql/logpostgres"
sleep 1