.PHONY: install run smoke pre-commit help

# ATTENTION: It must be TABS AND NOT SPACES before the commands, otherwise it will not work.

install: ## Install runtime dependencies
	pip install -r requirements.txt

run: ## Start the app on http://localhost:5000 (FLASK_DEBUG=1 for debug mode)
	python app.py

smoke: ## Same check CI runs: the home page responds
	python -c "import app; assert app.app.test_client().get('/').status_code == 200"

pre-commit: ## Run all pre-commit hooks
	pre-commit run --all-files

help: ## List available commands
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "} {printf "  %-12s %s\n", $$1, $$2}'
