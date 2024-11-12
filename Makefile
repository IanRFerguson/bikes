local:
	@echo "Starting Postgres..."
	@brew services start postgresql
	@echo "Running pipeline..."
	@python source/python/run_analytics.py

dev:
	@echo "Running pipeline..."
	@docker compose up