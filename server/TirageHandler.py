import json
from server.BaseHandler import BaseHandler
from server import jsonEncode
from TirageModele import Tirage

class TirageHandler(BaseHandler):
    def get(self):
        response = { 'tirages': [] }
        tirages = Tirage.query().order(-Tirage.datecreation).fetch()
        for tirage in tirages:
            response['tirages'].append({
                'nomtirage': tirage.nomtirage,
                'datecreation': str(tirage.datecreation)[0:19]
            })
        self.response.write(jsonEncode.encode(response))

    def post(self):
        mode = self.request.GET.get("mode", self.request.url.split("/")[-1].split('?')[0])
        if mode == "creertirage":
            lebody = json.loads(self.request.body)
            pseudo = str(lebody.get('pseudo')).lower()
            pseudo = pseudo.replace(" ", "")
            existe = Tirage.query(Tirage.nomtirage == pseudo).get()
            if existe == None:
                nomtirage = ""
            else:
                nomtirage = existe.nomtirage
            if pseudo != "" and pseudo != None and pseudo != "none" and pseudo != nomtirage:
                tirage = Tirage(nomtirage=pseudo)
                tirage.put()
                response = {
                    'message': 'ok'
                }
                self.response.write(jsonEncode.encode(response))
            else:
                if pseudo == "none":
                    response = {
                        'message': 'none'
                    }
                else:
                    response = {
                        'message': 'ko'
                    }

                self.response.write(jsonEncode.encode(response))

    def put(self):
        pass

    def delete(self):
        pass