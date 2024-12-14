#!/bin/bash

set -e

SECRETS_TARGET="./.dlt/secrets.toml"

# Check for secrets.toml
if [[ ! -f $SECRETS_TARGET  ]]; then
    cp ./.dlt/secets.toml.template $SECRETS_TARGET
    printf "\ndlt secrets.toml file created - fill this out before running!\n\n"
    exit 1
fi

# Check for local env file
if [[ ! -f local.env ]]; then
    touch local.env
    printf "\nlocal.env file created - fill this out before running!\n\n"
    exit 1
fi