__author__ = 'lorenzo'


import sys
sys.path.insert(0, 'lib')

import lib.falcon as falcon

from google.appengine.ext.webapp.util import run_wsgi_app


class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world!'


# Resources are represented by long-lived class instances
things = ThingsResource()

# falcon.API instances are callable WSGI apps
wsgi_app = api = falcon.API()

# things will handle all requests to the '/things' URL path
api.add_route('/things', things)


def main():
    run_wsgi_app(wsgi_app)

if __name__ == '__main__':
    main()