import json
from os.path import abspath, dirname, join
from pathlib import Path
from typing import Any, Dict, List

from flask import Response, render_template_string, request, abort
from flask.views import MethodView
from graphql.error.graphql_error import GraphQLError
from strawberry.schema.base import BaseSchema


class GraphQLAPI(MethodView):
    """Flask view that offers a graphql api service"""

    def __init__(self, schema: BaseSchema, use_playground=False):
        self.schema = schema
        self.use_playground = use_playground

    def get(self):
        """Serve graphiql to interact with the API"""
        if "text/html" in request.environ.get("HTTP_ACCEPT", ""):
            template = self._get_graphql_template()
            return render_template_string(template, REQUEST_PATH=request.full_path)
        else:
            abort(404)

    def _get_graphql_template(self):
        template = Path(__file__).parent.parent / 'static'
        template_name = 'playground' if self.use_playground else 'graphiql'
        graphiql_html_file = template / f'{template_name}.html'

        html_string = '<p>GraphiQL Error 👻</p>'
        with graphiql_html_file.open('r') as f:
            html_string = f.read()

        return html_string

    def post(self):
        """Answer graphql queries"""
        data = request.json

        query = data.get("query")
        variables = data.get("variables")
        operation_name = data.get("operationName")

        if not query:
            return Response("No valid query was provided for the request", 400)

        context = self.init_context()
        result = self.execute(
            query,
            variables,
            operation_name,
            context,
        )

        if result.errors:
            errors = self.handle_errors(result.errors)
            response = {
                'data': result.data,
                'errors': errors
            }
        else:
            response = {
                'data': result.data
            }

        return self.make_response(response)

    def init_context(self) -> Dict:
        """Initialize context with common data across resolvers"""
        return {
            'request': request,
            'redis': None,
        }

    def execute(self, query, variables, operation, context, root_value=None):
        return self.schema.execute_sync(
            query,
            variable_values=variables,
            context_value=context,
            operation_name=operation,
            root_value=root_value,
        )

    def handle_errors(self, errors: List[GraphQLError]) -> Dict[str, Any]:
        return [
            str(error)
            for error in errors
        ]

    def make_response(self, response):
        return Response(
            json.dumps(response),
            status=200,
            content_type="application/json",
        )
