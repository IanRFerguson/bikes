#!/bin/bash

set -e

# Check for local env file
if [[ ! -f local.env ]]; then
    cp ./local.env.template ./local.env
    printf "\nlocal.env file created - fill this out before running!\n\n"
    exit 1
fi