#! /usr/bin/env/ bash

alembic upgrade head
./deployment/scripts/prestart.sh
python3 ./cmd/bot/main.py
