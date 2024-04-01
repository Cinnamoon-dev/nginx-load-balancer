#!/usr/bin/env bash

readonly migrations_container="test1"
readonly others_containers=( $(cat compose.yaml | grep -G "container_name" | grep -v "nginx" | grep -v $migrations_container | grep -U -v "postgres_db" | cut -d ":" -f 2) )

docker compose up -d

sleep 15

docker cp $migrations_container:/api/migrations .

for i in ${others_containers[@]}; do
    docker cp migrations $i:/api
    docker exec -i $i flask db stamp head 
done

