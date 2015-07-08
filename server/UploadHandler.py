import json
import csv
import urllib2
from server.BaseHandler import BaseHandler
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import blobstore
from server import jsonEncode
from UploadModele import Upload

class UploadHandler(BaseHandler, blobstore_handlers.BlobstoreUploadHandler):
    def get(self):
        pass

    def post(self):
        mode = self.request.GET.get("mode", self.request.url.split("/")[-1].split('?')[0])
        if mode == "upload":
            url = 'https://docs.google.com/spreadsheets/d/1m9NK85BDWdvV3FXU93QVMKz3Ecl5XfD5RM2a1ao8UKw/export?format=csv'
            rep = urllib2.urlopen(url)
            moncsv = csv.reader(rep)
            for row in moncsv:
                for i in range(len(row)):
                    texte = str(row[i]) + ' colonne : ' + str(i)
                    print(texte)
            try:
                upload = self.get_uploads()[0]
                user_photo = Upload(image=upload.key())
                user_photo.put()

                self.redirect('/login')
            except:
                self.redirect('/')

    def put(self):
        pass

    def delete(self):
        pass
