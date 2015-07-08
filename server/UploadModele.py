from google.appengine.ext import ndb

class Upload(ndb.Model):
    image = ndb.BlobKeyProperty()
