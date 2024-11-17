
SHELL := bash
PATH += :$(HOME)/.local/bin

ACTIVATE = source .venv/bin/activate

all:
	echo "Welcome!"

.venv:
	which uv || curl -LsSf https://astral.sh/uv/install.sh | sh
	uv venv --python=python3.12

install: .venv
	$(ACTIVATE) && uv pip compile --quiet requirements.txt -o requirements.lock
	$(ACTIVATE) && uv pip install -r requirements.lock
	$(ACTIVATE) && pre-commit install

STRICT := --strict --ignore-missing-imports --no-namespace-packages

lint:
	$(ACTIVATE) && black . && isort . && ruff check
	$(ACTIVATE) && pyright .
	$(ACTIVATE) && mypy $(STRICT) .

# https://archive.ics.uci.edu/dataset/320/student+performance
STUDENT_PERF_URL = https://archive.ics.uci.edu/static/public/320/student+performance.zip

/tmp/student-mat.csv:
	curl -s $(STUDENT_PERF_URL) -o $@
	cd /tmp && unzip -o $@
	cd /tmp && unzip -o student.zip && rm -f student-merge.R

test: /tmp/student-mat.csv
	$(ACTIVATE) && python -m unittest */*/*_test.py
	$(ACTIVATE) && pytest

OUT = \
 /tmp/poultry_report.html \
 /tmp/student-mat.csv \
 /tmp/student* \
 /tmp/web_cache.sqlite \

clean:
	rm -f requirements.lock $(OUT)
	rm -rf .venv

.PHONY: all install lint clean
