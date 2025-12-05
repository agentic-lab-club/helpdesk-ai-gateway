build:
	@docker compose up --build -d

up:
	@docker compose up -d

logs:
	@docker compose logs -f

down:
	@docker compose down

remove:
	@docker compose down -v
	#@compose down --remove-orphans

exec-app:
	@docker exec -it backend_app sh

exec-db:
	@docker exec -it postgres_db psql -U postgres -d app_db
	#@docker exec -it postgres_db sh

test:
	@echo "Testing..."
	@poetry pytest
