from routes.create_reaction_comment_route import  create_comment_reaction_bp
from routes.get_comments_tweet_route import comment_get_bp
from routes.create_comment_route import comment_bp
from routes.update_comment_route import update_comment_bp
from routes.delete_comment_route import delete_comment_bp
from routes.delete_reaction_comment_route import reactions_bp
from routes.get_reactions_tweet_route import tweet_reactions_bp
from routes.create_reaction_tweet_route import reaction_bp
from routes.get_reactions_comment_route import comment_reaction_bp
from routes.delete_reaction_tweet_route import tweet_reaction_bp
from routes.reaction_stats_tweet_route import reaction_stats_bp
from routes.reaction_stats_comment_route import comment_reaction_stats_bp
from routes.check_user_reaction_route import reaction_check_bp 

blueprints =[ create_comment_reaction_bp, comment_get_bp, comment_bp,
             update_comment_bp, delete_comment_bp, reactions_bp,
             tweet_reactions_bp, reaction_bp, comment_reaction_bp,
             tweet_reaction_bp,reaction_stats_bp,comment_reaction_stats_bp, reaction_check_bp
            ]
