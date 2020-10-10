from flask import Flask
from graphql import get_introspection_query
import json

from strawapp.voyager_view import APIExplorer
from strawapp.flask_view import GraphQLAPI
from strawapp.app import schema


app = Flask(__name__, static_folder='static')


# Serve Graphiql IDE at /
graphiql = GraphQLAPI.as_view("graphql_view", schema=schema, use_playground=True)
app.add_url_rule("/", view_func=graphiql)


# Serve Explorer at /explore
introspection = schema.execute_sync(get_introspection_query())
explorer = APIExplorer.as_view("explorer_view", introspection=json.dumps({'data': introspection.data}))
app.add_url_rule("/explorer", view_func=explorer)


if __name__ == "__main__":
    app.run()
