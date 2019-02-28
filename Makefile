init:
	pip install pipenv
	pipenv install
	pipenv run pip uninstall numpy

test:
	pipenv run python manage.py test