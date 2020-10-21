from flask.views import MethodView
from pathlib import Path


class APIExplorer(MethodView):
    """Flask view that offers a graphql api service"""

    def __init__(self, introspection):
        self.introspection = introspection

    def get(self):
        """Serve graphiql to interact with the API"""
        template = self._get_voyager_template()
        return template.replace('{{introspection}}', self.introspection)

    def _get_voyager_template(self):
        voyager_html = Path(__file__).parent.parent / 'static' / 'voyager.html'
        html_string = '<p>Voyager Error 👻</p>'
        try:
            with voyager_html.open('r') as f:
                html_string = f.read()
        except Exception as e:
            print(f'{e!r}')

        return html_string
