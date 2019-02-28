init:
	pip install pipenv
	pipenv install
	pipenv run pip uninstall -y numpy

test:
	pipenv run python manage.py test