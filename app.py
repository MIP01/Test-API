from flask import Flask
from flask_cors import CORS
from route.user_routes import user_bp
from route.bangun_routes import bangun_bp
from route.film_routes import film_bp
from route.pesan_routes import pesan_bp
from flask_migrate import Migrate
from model import db

app = Flask(__name__)
app.json.sort_keys = False
CORS(app)

#Migrate func
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Test_API!",
        "API_documentation": "https://documenter.getpostman.com/view/24280418/2sAYJ3DMC9"
        "available_routes":
            "/api/v1/users",
            "/api/v1/bangun",
            "/api/v1/film",
            "/api/v1/pesan"
    })

#Regis route
app.register_blueprint(user_bp, url_prefix='/api/v1')
app.register_blueprint(bangun_bp, url_prefix='/api/v1')
app.register_blueprint(film_bp, url_prefix='/api/v1')
app.register_blueprint(pesan_bp, url_prefix='/api/v1')

# gunakan saat local development
#if __name__ == '__main__':
    #app.run(port=5000)