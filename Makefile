run:
	@python manage.py migrate
	@python manage.py runserver

run-docker:
	@docker-compose up --build

test:
	@pytest

