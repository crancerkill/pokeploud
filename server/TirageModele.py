from google.appengine.ext import ndb

class Tirage(ndb.Model):
    nomtirage = ndb.StringProperty()
    datecreation = ndb.DateTimeProperty(auto_now_add=True)
