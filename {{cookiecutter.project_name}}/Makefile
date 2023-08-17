SHELL := /bin/bash
.DEFAULT_GOAL := format

isort = poetry run isort
ruff = poetry run ruff --fix
black = poetry run black
managepy = poetry run python manage.py
startdb = docker compose up -d

.PHONY: format
format:
	$(black) .
	$(isort) -sl .
	$(ruff) .
	$(isort) -m 3 .
	$(black) .

.PHONY: r
r:
	$(startdb)
	@$(managepy) runserver

.PHONY: rn
rn:
	@xdg-open http://127.0.0.1:8000/
	@$(MAKE) r

.PHONY: sudo
sudo:
	@$(managepy) createsuperuser

.PHONY: mm
mm:
	$(startdb)
	@$(managepy) makemigrations

.PHONY: m
m:
	$(startdb)
	@$(managepy) migrate

.PHONY: unmigrate
unmigrate:
	@docker compose down -v

.PHONY: um
um: unmigrate

.PHONY: urls
urls:
	@$(managepy) show_urls

.PHONY: %
%:
	@$(managepy) $*
