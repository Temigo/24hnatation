#!/bin/sh
docker exec -ti nat24h sh -c 'cd /srv/app/server && python manage.py shell_plus'
