.PHONY: build run

build:
	docker build . -t pyconar-graphql

run:
	docker run -it --rm -v $(PWD):/app -p 5050:5050 pyconar-graphql

run-dev:
	FLASK_APP=strawapp.flask_app FLASK_DEBUG=1 flask run

tunnel:
	# Remember to add ngrok's path to your $PATH for this target to work
	ngrok http 5050

