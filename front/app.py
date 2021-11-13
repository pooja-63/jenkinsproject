from flask import Flask
from flask_bootstrap import Bootstrap
from routes import blueprint
app = Flask(__name__, static_folder='static')

app.config['UPLOAD_FOLDER'] = 'static/images'

app.register_blueprint(blueprint)
bootstrap = Bootstrap(app)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
