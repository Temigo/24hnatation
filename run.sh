#!/bin/sh
docker build -t binetreseau/nat24h .
docker run --name="nat24h-db" -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=django -d mysql
docker run -p 24000:8000 --name="nat24h" --link="nat24h-db:mysqldb" binetreseau/nat24h
