from google.appengine.ext import db

class Story(db.Model):
    title = db.StringProperty(required=True)
    link = db.StringProperty(required=True)
    tweet = db.StringProperty(required=True)
    saved = db.DateTimeProperty(required=True, auto_now=True)
