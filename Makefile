docker-build:
	# Build the Docker image
	docker build -t app .

refresh-dev:
	# Stop the dev server
	docker-compose down
	# Delete the docker image 'app'
	docker rmi app
	# Start the dev server
	docker-compose up -d --force-recreate --remove-orphans

start-dev:
	# Start the dev server
	docker-compose up -d --force-recreate --remove-orphans

stop-dev:
	# Stop the dev server
	docker-compose down

logs-dev:
	# Watch container logs
	docker-compose logs -f
