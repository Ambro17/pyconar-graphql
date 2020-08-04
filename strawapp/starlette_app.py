from starlette.applications import Starlette

from starlette.middleware.cors import CORSMiddleware
from strawberry.asgi import GraphQL

from .app import schema


app = Starlette(debug=True)
app.add_middleware(
    CORSMiddleware, allow_headers=["*"], allow_origins=["*"], allow_methods=["*"]
)

graphql_app = GraphQL(schema, debug=True)

paths = ["/", "/graphql"]

for path in paths:
    app.add_route(path, graphql_app)

# Run it with uvicron module:app_attribute
