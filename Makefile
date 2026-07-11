SHELL := /bin/bash
.DEFAULT_GOAL := help

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
ROLE ?= all

.PHONY: help setup setup-all doctor install-litellm build-vllm start-vllm stop-vllm logs-vllm litellm acceptance acceptance-print endpoint-probe gpu-preflight eval-local tech-doctor scaffold context repo-check lint clean

help:
	@printf 'Zynclaw commands\n'
	@printf '\nNon-technical / workflow:\n'
	@printf '  make help                         Show this menu\n'
	@printf '  make scaffold WORK="task name"    Create a full work-item folder\n'
	@printf '  make context ROLE=engineering     Export a role-specific agent context pack\n'
	@printf '  make repo-check                   Validate required docs and local links\n'
	@printf '\nTechnical setup:\n'
	@printf '  make setup                        Create/update .env and check basics\n'
	@printf '  make install-litellm              Install LiteLLM into .venv\n'
	@printf '  make build-vllm                   Build the patched vLLM image\n'
	@printf '  make start-vllm                   Start vLLM with Docker Compose\n'
	@printf '  make litellm                      Start LiteLLM in the foreground\n'
	@printf '\nValidation:\n'
	@printf '  make doctor                       Check prerequisites and reachability\n'
	@printf '  make endpoint-probe               Probe LiteLLM/vLLM health and metrics\n'
	@printf '  make acceptance                   Validate structured tool calls\n'
	@printf '  make eval-local                   Run optional promptfoo evals\n'
	@printf '  make tech-doctor                  Check optional eval/security tools\n'
	@printf '  make lint                         Run repo validation checks\n'

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

eval-local:
	./scripts/run_promptfoo_eval.sh

tech-doctor:
	./scripts/tech_doctor.sh

scaffold:
	python3 scripts/scaffold_work_item.py "$(WORK)"

context:
	python3 scripts/export_context.py --role "$(ROLE)"

repo-check:
	python3 scripts/check_structure.py

lint:
	python3 -m py_compile scripts/*.py
	bash -n scripts/*.sh
	python3 scripts/check_structure.py

clean:
	rm -rf .pytest_cache .ruff_cache scripts/__pycache__ tmp
