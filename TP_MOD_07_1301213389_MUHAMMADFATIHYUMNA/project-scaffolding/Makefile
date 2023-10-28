install:
	pip install --upgrade pip && pip install -r requirements.txt

post-install:
	python -m textblob.download_corpora

format:
	black *.py mylib/*.py

lint:
	pylint --disable=R,C main.py mylib/logic.py

test:
	python -m pytest -vv --cov=mylib --cov=main test_*.py

build:
	docker build -t deploy-fastapi .

run:
	docker run -p 127.0.0.1:8080:8080 deploy-fastapi

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 085141973272.dkr.ecr.us-east-1.amazonaws.com
	docker build -t wiki-fastapi .
	docker tag wiki-fastapi:latest 085141973272.dkr.ecr.us-east-1.amazonaws.com/wiki-fastapi:latest
	docker push 085141973272.dkr.ecr.us-east-1.amazonaws.com/wiki-fastapi:latest

all: install post-install lint test deploy
