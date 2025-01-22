from flask import Blueprint

bp = Blueprint('routes', __name__)

from src.routes.meta import meta
from src.routes.tweetlist import get_tweet_list
from src.routes.tweet import create_tweet