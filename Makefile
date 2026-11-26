run-api:
	uvicorn api.fast:app --reload

build-docker-local:
	docker build -t ${IMAGE_NAME}:dev .

docker-run:
	docker run -p 8001:8080 ${IMAGE_NAME}:dev

docker-build-cloud:
	docker build --platform linux/amd64 -t ${GAR_IMAGE_NAME}:prod .

docker-push:
	docker push ${GAR_IMAGE_NAME}:prod

docker-deploy:
	gcloud run deploy ${CLOUD_RUN_SERVICE_NAME} \
		--image ${GAR_IMAGE_NAME}:prod \
		--allow-unauthenticated \
		--region ${GCP_REGION}
