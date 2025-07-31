run:
	@docker-compose up --build

test:
	@docker-compose exec web pytest

makemigrations:
	@docker-compose exec web python manage.py makemigrations

migrate:
	@docker-compose exec web python manage.py migrate

createsuperuser:
	@docker-compose exec web python manage.py createsuperuser

shell:
	@docker-compose exec web python manage.py shell
