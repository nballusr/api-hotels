SHELL=/bin/bash


COLOR_NC:=\033[0m
COLOR_GREEN:=\033[0;32m

.PHONY: docker-build
docker-build:
	docker compose build

.PHONY: install
install: docker-build start

.PHONY: start
start:
	test -f .env.local || cp .env .env.local
	docker compose run --rm python poetry install --no-root
	docker compose up -d --remove-orphans --force-recreate
	docker compose run --rm python poetry run alembic upgrade head
	docker compose run --rm -e APP_ENV=test python poetry run alembic upgrade head

	@echo "####################################################################"
	@echo ""
	@echo -e "$(COLOR_GREEN) Done! $(COLOR_NC)"
	@echo -e "  - API available at http://localhost:8080"
	@echo -e "  - API doc available at http://localhost:8080/api/docs"
	@echo ""
	@echo "####################################################################"

.PHONY: stop
stop:
	docker compose stop

.PHONY: shell
shell:
	docker compose exec python poetry shell

.PHONY: new-shell
new-shell:
	docker compose run --rm python bash -c "poetry shell"

.PHONY: clean
clean: stop
	docker compose rm -f

.PHONY: restart
restart: clean start

.PHONY: pytest
pytest:
	docker compose run --rm -e APP_ENV=test python poetry run pytest

.PHONY: acceptance
acceptance:
	docker compose run --rm -e APP_ENV=test python poetry run behave --tags=-skip tests/acceptance

.PHONY: tests
tests: pytest acceptance
