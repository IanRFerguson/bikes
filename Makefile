# Run the pipeline locally (into a local Postgres)
local:
	@echo "* Running pre-build checks..."
	@./deploy/run_checks.sh

	@echo "* Starting Postgres..."
	@brew services start postgresql

	@echo "* Running pipeline..."
	@python src/python/run_analytics.py


# Run the pipeline via Docker Compose
dev:
	@echo "* Running pre-build checks..."
	@./deploy/run_checks.sh
	
	@echo "* Running pipeline..."
	@ if [ ! -z $(build) ]; then 	\
		docker compose up --build; 	\
	else 							\
		docker compose up; 			\
	fi