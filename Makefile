init:
	pip install pipenv
	pipenv install
	pipenv clean

test:
	pipenv run python manage.py test