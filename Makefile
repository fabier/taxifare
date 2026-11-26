run-api:
	uvicorn api.fast:app --reload


build-docker-local:
	docker build -t ${IMAGE_NAME}:dev .

docker-run:
	docker run -p 8001:8080 ${IMAGE_NAME}:dev
