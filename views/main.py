import os
import re

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from models import models
import settings

class MainPage(webapp.RequestHandler):
    def get(self):
        template_dict = {}
        template_dict['tweets'] = []
        template_dict['settings'] = settings
        
        recent_stories = models.Story.all().fetch(10)
        tweets = [s.tweet for s in recent_stories]

        for i,tweet in enumerate(tweets):
            matches = re.search(r'^(.+)(http\:\/\/(trib\.in|bit\.ly)\/(.?)+$)', tweet)

            body = matches.group(1)
            link = matches.group(2)

            template_dict['tweets'].append({
                'body': body, 
                'link': link
                })
            
        path = os.path.join(settings.TEMPLATE_DIR, 'index.html')
        self.response.out.write(template.render(path, template_dict))
                                            
application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
