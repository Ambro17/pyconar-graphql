from .flask_view import GraphQLAPI
from flask import Flask
from flask_cors import CORS

from .app import schema

app = Flask(__name__, static_folder='static')

# NOT SECURE AT ALL!! don't copy paste!
CORS(app, origins='null') # <-- Danger
# I did this just to allow graphql-rover to introspect the schema in a LOCAL environment.
# See https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#Preflighted_requests for why you be careful with CORS


app.add_url_rule(
    "/",
    view_func=GraphQLAPI.as_view("graphql_view", schema=schema, use_playground=False)
)

if __name__ == "__main__":
    app.run(debug=True)
