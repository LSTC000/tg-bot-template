#! /usr/bin/env/ bash

./deployment/scripts/wait-for-it.sh POSTGRES_HOST:POSTGRES_PORT
alembic upgrade head
./deployment/scripts/prestart.sh
python3 ./cmd/bot/main.py
