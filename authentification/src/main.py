import os

from dotenv import load_dotenv

from config import app
from routes import route
load_dotenv()

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.register_blueprint(route)
    app.run(host="0.0.0.0", debug=debug_mode, port=5000)

