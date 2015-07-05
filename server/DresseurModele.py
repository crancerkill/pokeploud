from google.appengine.ext import ndb

class Dresseur(ndb.Model):
    tirage = ndb.KeyProperty(kind='Tirage')
    nomig = ndb.StringProperty()
    codeami = ndb.StringProperty()
