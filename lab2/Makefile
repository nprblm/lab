all: install test run deploy

install:
	@echo "Installing python 3.8"
	pipenv --python 3.8
	@echo "Installing requests"
	pipenv install requests
	@echo "Installing ntpli"
	pipenv install ntplib
	@echo "Installing pytes"
	pipenv install pytest

test:
	@echo "Starting tests.py and add results to results.txt"
	pipenv run pytest tests/tests.py > results.txt

run:
	@echo "Run app.py and add results to results.txt"
	pipenv run python app.py >> results.txt

deploy:
	@echo "adding results.txt to rep"
	git add results.txt
	@echo "git commit"
	git commit -a -m "add result to results.txt"
	@echo "git push"
	git push