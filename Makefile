
SHELL := bash
PATH += :$(HOME)/.local/bin

ACTIVATE = source .venv/bin/activate

all:
	echo "Welcome!"

install:
	which uv || curl -LsSf https://astral.sh/uv/install.sh | sh
	uv venv --python=python3.12
	uv pip compile --quiet requirements.in -o requirements.lock
	uv pip install -r requirements.lock
	$(ACTIVATE) && pre-commit install

lint:
	$(ACTIVATE) && black . && ruff check && isort .

test:
	$(ACTIVATE) && python -m unittest */*_test.py
	$(ACTIVATE) && pytest

clean:
	rm -rf .venv

.PHONY: all install lint clean
