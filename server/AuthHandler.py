import json
from server.BaseHandler import BaseHandler
from server import jsonEncode

class AuthHandler(BaseHandler):
    def get(self):
        self.response.write('')

    def post(self):
        mode = self.request.GET.get("mode", self.request.url.split("/")[-1].split('?')[0])
        if mode == 'connexion':
            self.setSessionParameter('user','crancer')
        elif mode == 'affuser':
            user = self.getSessionUser()
            response = {
                'user': user
            }
            self.response.write(jsonEncode.encode(response))

    def put(self):
        pass

    def delete(self):
        pass
