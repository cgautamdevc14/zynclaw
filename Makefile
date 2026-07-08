SHELL := /bin/bash

ifneq (,$(wildcard .env))
include .env
export
endif

VLLM_IMAGE ?= vllm-qwen36:26.06-py3-patched
VLLM_COMPOSE ?= infra/vllm/compose.example.yaml
LITELLM_CONFIG ?= infra/litellm/config.example.yaml
LITELLM_PORT ?= 4000
LITELLM_BIN := $(shell if [ -x .venv/bin/litellm ]; then echo .venv/bin/litellm; elif command -v litellm >/dev/null 2>&1; then command -v litellm; else echo litellm; fi)
WORK ?= local-agent-task

.PHONY: setup setup-all doctor install-litellm build-vllm start-vllm stop-vllm logs-vllm litellm acceptance acceptance-print endpoint-probe gpu-preflight scaffold repo-check lint clean

setup:
	./scripts/setup.sh

setup-all:
	./scripts/setup.sh --install-litellm --build-vllm --start-vllm

doctor:
	./scripts/doctor.sh

install-litellm:
	./scripts/install_litellm.sh

build-vllm:
	docker build -t $(VLLM_IMAGE) -f infra/vllm/Dockerfile.ngc-patched .

start-vllm:
	docker compose --env-file .env -f $(VLLM_COMPOSE) up -d

stop-vllm:
	docker compose --env-file .env -f $(VLLM_COMPOSE) down

logs-vllm:
	docker compose --env-file .env -f $(VLLM_COMPOSE) logs -f vllm-qwen36

litellm:
	$(LITELLM_BIN) --config $(LITELLM_CONFIG) --port $(LITELLM_PORT)

acceptance:
	python3 scripts/acceptance.py

acceptance-print:
	python3 scripts/acceptance.py --print-response

endpoint-probe:
	python3 scripts/endpoint_probe.py

gpu-preflight:
	./scripts/gpu_preflight.sh

scaffold:
	python3 scripts/scaffold_work_item.py "$(WORK)"

repo-check:
	python3 scripts/check_structure.py

lint:
	python3 -m py_compile scripts/*.py
	bash -n scripts/*.sh
	python3 scripts/check_structure.py

clean:
	rm -rf .pytest_cache .ruff_cache scripts/__pycache__ tmp
