# -*- coding: utf-8 -*-
import json
from server.BaseHandler import BaseHandler
from server import jsonEncode
from server.DresseurModele import Dresseur
from server.TirageModele import Tirage

class DresseurHandler(BaseHandler):

    def get(self):
        response = { 'dresseurs': [] }
        dresseurs = Dresseur.query().fetch()
        response['dresseurs'] = dresseurs
        self.response.write(jsonEncode.encode(response))

    def post(self):
        mode = self.request.GET.get("mode", self.request.url.split("/")[-1].split('?')[0])
        if mode == 'addDresseur':
            lebody = json.loads(self.request.body)
            if str(lebody.get('nomig')) != "" and str(lebody.get('codeami')) != "" and str(lebody.get('tirage')) != "" and lebody.get('nomig') != None and lebody.get('codeami') != None and lebody.get('tirage') != None:
                tirage = Tirage.query(Tirage.nomtirage == lebody.get('tirage')).get()
                letirage = tirage.key
                dresseur = Dresseur(tirage=letirage,
                                    nomig=lebody.get('nomig'),
                                    codeami=lebody.get('codeami'))
                dresseur.put()
                response = {
                    'message': 'ok'
                }
            else:
                response = {
                    'message': 'ko'
                }
            self.response.write(jsonEncode.encode(response))
        elif mode == 'tirageAlea':
            lebody = json.loads(self.request.body)
            response = { 'dresseurs': [] }
            tirage = Tirage.query(Tirage.nomtirage == lebody.get('tirage')).get()
            letirage = tirage.key
            dresseurs = Dresseur.query(Dresseur.tirage == letirage).fetch()
            response['dresseurs'] = dresseurs
            self.response.write(jsonEncode.encode(response))

    def put(self):
        pass

    def delete(self):
        pass