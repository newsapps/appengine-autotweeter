import logging
logging.getLogger().setLevel(logging.DEBUG)
from models import models
from xml.dom import minidom

from google.appengine.api import urlfetch
import bitly
import twitter

import settings

MAX_TWEET_LENGTH = 140

def shorten_url(url):
    """
    Shorten a url using bit.ly.
    """
    api = bitly.Api(**settings.BITLY_AUTH)
    short = api.shorten(url)

    return short

def tweet(text):
    """
    Send a tweet.
    """
    api = twitter.Api(cache=None, **settings.TWITTER_AUTH)   
    api.PostUpdate(text)

def main():
    """
    Grab new posts and tweet them.
    """
    actually_tweet = True

    # Don't tweet if the script has never stored a result (first run)
    if not models.Story.all().count(1):
        logging.info('First run, not tweeting stories.')
        actually_tweet = False

    # Fetch latest RSS feed
    response = urlfetch.fetch(settings.RSS_URL)
    xml_str = unicode(response.content, errors='ignore')    # TKTK?
    xml_dom = minidom.parseString(xml_str)

    nodes = list(xml_dom.getElementsByTagName('item'))

    new_tweets = 0

    for node in nodes:
        link = node.getElementsByTagName('link')[0].childNodes[0].data

        existing = models.Story.gql("WHERE link = :link", link=link)
        if existing.count(): continue

        new_tweets += 1

        title = node.getElementsByTagName('title')[0].childNodes[0].data
        link = node.getElementsByTagName('link')[0].childNodes[0].data
        logging.debug(title)
        logging.debug(link)
        short_link = shorten_url(link)

        max_title_length = MAX_TWEET_LENGTH - (len(short_link) + 1)
        if len(title) > max_title_length:
            title = title[:max_title_length - 3] + '...'

        tweet_text = '%s %s' % (title, short_link)

        logging.debug(tweet_text)
        logging.debug(len(tweet_text))

        if actually_tweet:
            logging.debug('Tweeting: %s' % tweet_text)
            tweet(tweet_text)

        new_story = models.Story(title=title, link=link, tweet=tweet_text)
        new_story.put()

    logging.info('Stored %i new tweets' % new_tweets)

if __name__ == "__main__":
    main()
