init:
	pip install pipenv
	pipenv install

test:
	pipenv run python manage.py test
