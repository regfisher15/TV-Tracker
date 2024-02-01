#!/bin/bash

set -e

env_file=".env"

if [ -f "$env_file" ]; then
    source "$env_file"
else
    echo "You forgot the .env" && exit
fi

# no need to .env this
local_repo_path="../airbyte"

# check for repo
if [ -d "$local_repo_path" ]; then
    # If exists, pull
    cd "$local_repo_path"
    git pull
else
    # else clone
    cd ".."
    git clone "$OUR_AIRBYTE"
    cd "airbyte"
fi

# call with --debug-ab to watch airbyte logs, rather than our logs
# highly recommended if you haven't pulled airbyte images already
if [[ "$1" == "--debug-ab" ]]; then
    ./run-ab-platform.sh > /dev/null 2>&1 &
    cd "../495-website"
    docker compose up --build --detach

else
    ./run-ab-platform.sh > /dev/null 2>&1 &
    cd "../495-website"
    docker compose up --build

fi