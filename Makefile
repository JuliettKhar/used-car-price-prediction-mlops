.PHONY: install train pipeline predict monitor test integration-test docker-build docker-run

install:
	pip install -r requirements.txt

train:
	python src/train.py

pipeline:
	python src/pipeline.py

predict:
	python src/predict.py

monitor:
	python src/monitor.py

test:
	pytest tests/

integration-test:
	./integration_tests/test_docker_prediction.sh

docker-build:
	docker build -t used-car-price-prediction .

docker-run:
	docker run --rm used-car-price-prediction

lint:
	ruff check src tests

format:
	ruff format src tests