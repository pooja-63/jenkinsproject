from flask import Flask
from routes import book_blueprint
from models import db,init_app,Book
from flask_migrate import Migrate
import os

app = Flask(__name__)


db_user = os.environ.get('POSTGRES_USER')
db_psw = os.environ.get('POSTGRES_PASSWORD')
db_host = os.environ.get('db_name')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{0}:{1}@postgres/{2}'.format(
    db_user, db_psw, db_host
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(book_blueprint)
init_app(app)

migrate = Migrate(app,db)

if __name__ == '__main__':
	
	app.run(host='0.0.0.0', port=5001)

