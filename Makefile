.PHONY: acceptance lint

acceptance:
	python3 scripts/acceptance.py

lint:
	python3 -m py_compile scripts/acceptance.py
