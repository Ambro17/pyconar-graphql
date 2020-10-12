# PyconAr GraphQL Playground
`PyconAr GraphQL Playground` is a playground for anyone who wants to learn graphql interactively.

![Screenshot](strawapp/static/demo.png)
The repo has different kind of query resolvers, backed by
- DB Models
- JSON Files
- REST Calls
This is to demonstrate that there are no hard constraints on implementation details. 
We're free to do whatever fits better to our environment.

[Live Demo](https://pyconar.herokuapp.com/)


## About GraphQL
[GraphQL](https://graphql.org/) is a new paradigm in API Design that is rapidly growing in popularity.
Although it's not a replacement of REST, it does help solve some of its most frequent problems.
I hope that exploring the API you can get a taste of the benefits of GraphQL and perhaps motivate you to write your own GraphQL PoC for your next big project.


## Usage
To run the server follow these steps:
```python
python3.6 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP="strawapp.app:create_app()"
flask run
```
If you have docker installed you can start it with
```bash
docker build . -t pyconar-graphql
docker run -it -p 5050:5050 pyconar-graphql
```
You can also deploy to heroku with just one click

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Ambro17/pyconar-graphql/tree/master)


## Features
- IDE in Browser. _To explore the API interactively_
- Interactive Graph Explorer. _A visually compelling view of the API_
- Mutation Example. _Useful Patterns to alter data_
- Error Handling. _HTTP, what's that?_

## TODO
- Auth
- DoS Protection
- Remove custom GraphiQL
