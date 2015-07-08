import logging
import os
import jinja2
import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from server.DresseurHandler import DresseurHandler
from server.TirageHandler import TirageHandler
from server.AuthHandler import AuthHandler
from server.UploadHandler import UploadHandler

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(os.path.dirname(__file__))),
    variable_start_string='[[',
    variable_end_string=']]'
)

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('/index.html')
        self.response.out.write(template.render({}))

application = webapp2.WSGIApplication([
    ('/dresseur.*', DresseurHandler),
    ('/tirage.*', TirageHandler),
    ('/service/connexion.*', AuthHandler),
    ('/upload.*', UploadHandler),
    ('/.*', MainHandler),
], config=config, debug=False)


def main():
    logging.getLogger().setLevel(logging.DEBUG)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
