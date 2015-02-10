#!/bin/sh
git pull &&
docker build -t binetreseau/nat24h . &&
docker stop nat24h &&
docker rm nat24h &&
docker run -p 24000:8000 --name="nat24h" --link="nat24h-db:mysqldb" -d binetreseau/nat24h
