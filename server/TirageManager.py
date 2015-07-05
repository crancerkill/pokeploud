from google.appengine.ext import ndb
from server.TirageModele import Tirage

def QueryByNomTirage(nomtirage):
    query = Tirage.query(Tirage.nomtirage == nomtirage).fetch()

    return query.key