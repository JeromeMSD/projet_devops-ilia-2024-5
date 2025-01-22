run:
	docker run -p 8080:5000 --name tweet --rm tweet
build-run:
	docker build -t tweet -f ./Dockerfile . 
dev:
	docker run -p 8080:5000 -e FLASK_APP="/app/src/main.py" -v .:/app --name tweet-dev --rm tweet-dev
build-dev:
	docker build -t tweet-dev -f ./Dockerfile.dev . 
test:
	docker run -v $(shell pwd):/app -e PYTHONPATH=/app --name tweet-test --rm tweet-test

build-test:
	docker build -t tweet-test -f ./Dockerfile.test . 
swagger:
	docker run -p 80:8080 -e SWAGGER_JSON=/doc/swagger.yaml --name tweet_swagger --rm -v ./swagger.yaml:/doc/swagger.yaml swaggerapi/swagger-ui