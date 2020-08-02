from strawberry.flask.views import GraphQLView
from flask import Flask

from .app import schema

app = Flask(__name__)


app.add_url_rule(
    "/", 
    view_func=GraphQLView.as_view("graphql_view", schema=schema)
)

if __name__ == "__main__":
    app.run(debug=True)