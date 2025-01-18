from routes.get_reactions_route import tweet_reaction_bp
from routes.comment_route import comment_bp
from reaction.supp_comment_route import supp_comment_bp
from routes.ajouter_reactions_route import reaction_bp

blueprints =[ tweet_reaction_bp, comment_bp,reaction_bp,supp_comment_bp ]
