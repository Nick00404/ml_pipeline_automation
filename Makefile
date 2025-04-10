build:
	docker build -t ml_pipeline_automation .

run:
	docker-compose up

test:
	pytest tests/
