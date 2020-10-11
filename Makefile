.PHONY: build run run-dev tunnel clean-pyc

build:
	docker build . -t pyconar-graphql

run:
	docker run -it --rm -v $(PWD):/app -p 5050:5050 pyconar-graphql

run-dev:
	FLASK_APP="strawapp.app:create_app()" FLASK_DEBUG=1 flask run

tunnel:
	# Remember to add ngrok's path to your $PATH for this target to work
	ngrok http 5050

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete 
	find . -name '*~' -delete
	find . -name '__pycache__' -delete