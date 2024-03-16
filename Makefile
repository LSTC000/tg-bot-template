PYTHON=python3

ALEMBIC=alembic

DC-LOCAL=docker compose -f ./deployment/docker-compose.local.yaml
DC-PROD=docker compose -f ./deployment/docker-compose.prod.yaml

.PHONY: bot
bot-run:
	$(PYTHON) ./cmd/bot/main.py

.PHONY: lint
lint-run:
	black . && isort . && ruff .

.PHONY: alembic
alembic-head:
	$(ALEMBIC) upgrade head
alembic-down:
	$(ALEMBIC) downgrade -1
alembic-revision:
	$(ALEMBIC) revision --autogenerate -m $(DESC)

.PHONY: docker
docker-local:
	$(DC-LOCAL) up -d --build
docker-local-build:
	$(DC-LOCAL) build
docker-local-up:
	$(DC-LOCAL) up -d
docker-local-stop:
	$(DC-LOCAL) stop
docker-local-start:
	$(DC-LOCAL) start
docker-local-down:
	$(DC-LOCAL) down
docker-local-down-v:
	$(DC-LOCAL) down -v
docker-local-logs:
	$(DC-LOCAL) logs
docker-local-logs-f:
	$(DC-LOCAL) logs -f

docker-prod:
	$(DC-PROD) up -d --build
docker-prod-build:
	$(DC-PROD) build
docker-prod-up:
	$(DC-PROD) up -d
docker-prod-stop:
	$(DC-PROD) stop
docker-prod-start:
	$(DC-PROD) start
docker-prod-down:
	$(DC-PROD) down
docker-prod-down-v:
	$(DC-PROD) down -v
docker-prod-logs:
	$(DC-PROD) logs
docker-prod-logs-f:
	$(DC-PROD) logs -f
