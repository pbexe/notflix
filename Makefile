init:
	pip install pipenv
	pipenv install
	pipenv uninstall numpy

test:
	pipenv run python manage.py test