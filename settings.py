import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

FEEDS = [{
    'rss_url': 'http://www.TKTK.com/rss2.0.xml',
    'bitly_auth': {
        'login': 'TKTK',
        'apikey': 'TKTK',
    },
    'twitter_auth': {
        'consumer_key': 'TKTK',
        'consumer_secret': 'TKTK',
        'access_token_key': 'TKTK',
        'access_token_secret': 'TKTK',
    }
}]
