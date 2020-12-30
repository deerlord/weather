frontend_build:
	docker rm weather:latest
	docker build --rm . --tag="weather:latest"

frontend_deploy:
	docker run -p 3000:3000 weather:latest

frontend_all: frontend_build frontend_deploy