#!/bin/bash

echo "pulling updates"
git pull

branch=$(git branch --show-current)
export branch=$branch
echo $branch

echo "docker-compose up --build -d"
docker-compose --env-file .env.$branch up --build -d
