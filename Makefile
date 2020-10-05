.PHONY: build run

build:
	docker build . -t graphql-demo

run:
	docker run -it --rm -v $(PWD):/app -p 5050:5050 graphql-demo

explorer:
	echo "TODO"

docs:
	echo "TODO"