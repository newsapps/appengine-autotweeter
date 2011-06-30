import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

FEEDS = [{
    'rss_url': 'http://www.TKTK.com/rss2.0.xml',
    'bitly_auth': {
        'login': 'TKTK',
        'apikey': 'TKTK',
    },
    'twitter_auth': {
        # Note: these consumer keys need to be repeated for each feed (could be refactored)
        'consumer_key': 'TKTK',
        'consumer_secret': 'TKTK',
        # Get access tokens using the get_access_token.py script
        'access_token_key': 'TKTK',
        'access_token_secret': 'TKTK',
    }
}]
