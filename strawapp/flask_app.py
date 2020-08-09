from .flask_view import GraphQLAPI
from flask import Flask

from .app import schema

app = Flask(__name__, static_folder='static')


app.add_url_rule(
    "/",
    view_func=GraphQLAPI.as_view("graphql_view", schema=schema, use_playground=False)
)

if __name__ == "__main__":
    app.run(debug=True)
