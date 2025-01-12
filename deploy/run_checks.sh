#!/bin/bash

set -e

SECRETS_TARGET="./.dlt/secrets.toml"
RAISE=false

# Check for secrets.toml
if [[ ! -f $SECRETS_TARGET  ]]; then
    cp ./.dlt/secets.toml.template $SECRETS_TARGET
    printf "\nCreated secrets.toml file in .dlt folder...\n\n"
fi

# Check for local env file
if [[ ! -f local.env ]]; then
    cp ./local.env.template ./local.env
    printf "\nlocal.env file created - fill this out before running!\n\n"
    RAISE=true
fi