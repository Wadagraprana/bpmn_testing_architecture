.PHONY: env install dev run lint format test shell clean upgrade help

PYTHON ?= python
VENV_DIR := .venv

ifeq ($(OS),Windows_NT)
    VENV_BIN := $(VENV_DIR)\Scripts
    PATH_SEP := \\
else
    VENV_BIN := $(VENV_DIR)/bin
    PATH_SEP := /
endif

PIP := $(VENV_BIN)$(PATH_SEP)pip
FLASK := $(VENV_BIN)$(PATH_SEP)flask
GUNICORN := $(VENV_BIN)$(PATH_SEP)gunicorn
PYTEST := $(VENV_BIN)$(PATH_SEP)pytest
BLACK := $(VENV_BIN)$(PATH_SEP)black
ISORT := $(VENV_BIN)$(PATH_SEP)isort
FLAKE8 := $(VENV_BIN)$(PATH_SEP)flake8

env:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Creating virtual environment..."; \
		$(PYTHON) -m venv $(VENV_DIR); \
	fi

install: env
	@echo "Installing dependencies..."
	@$(PIP) install --upgrade pip
	@$(PIP) install -r requirements-dev.txt

upgrade: env
	@echo "Upgrading pip and dependencies..."
	@$(PIP) install --upgrade pip setuptools wheel
	@$(PIP) install --upgrade -r requirements-dev.txt

dev: env
	@echo "Running Flask development server..."
	@$(FLASK) run

run: env
	@echo "Running Gunicorn production server..."
	@$(GUNICORN) --bind 0.0.0.0:5000 --workers 4 'main:app'

lint: env
	@echo "Linting code with flake8..."
	@$(FLAKE8) app/ tests/

format: env
	@echo "Formatting code with black and isort..."
	@$(BLACK) app/ tests/
	@$(ISORT) app/ tests/

test: env
	@echo "Running tests with pytest..."
	@$(PYTEST) --cov=app tests/

shell: env
	@$(FLASK) shell

clean:
	@echo "Cleaning virtualenv and cache files..."
ifeq ($(OS),Windows_NT)
	@if exist $(VENV_DIR) rmdir /s /q $(VENV_DIR)
	@if exist .mypy_cache rmdir /s /q .mypy_cache
	@if exist .pytest_cache rmdir /s /q .pytest_cache
	@if exist __pycache__ rmdir /s /q __pycache__
	@if exist htmlcov rmdir /s /q htmlcov
	@if exist .coverage del /f /q .coverage
else
	@rm -rf $(VENV_DIR) .mypy_cache .pytest_cache __pycache__ htmlcov .coverage
endif

help:
	@echo "Available commands:"
	@echo "  make env       # Create python virtual environment"
	@echo "  make install   # Install dev requirements"
	@echo "  make dev       # Run Flask dev server"
	@echo "  make run       # Run Gunicorn production server"
	@echo "  make lint      # Run flake8 linting"
	@echo "  make format    # Format code (black + isort)"
	@echo "  make test      # Run tests with pytest"
	@echo "  make shell     # Flask shell"
	@echo "  make clean     # Remove virtualenv and caches"
	@echo "  make upgrade   # Upgrade pip and all dependencies"
	@echo "  make help      # Show this help message"

.DEFAULT_GOAL := help