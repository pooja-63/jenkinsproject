from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

def init_app(app):
	db.app = app
	db.init_app(app)
	db.create_all()
class Book(db.Model):
	__tablename__='book_details'
	id=db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String(255), unique=True, nullable=False)
	slug=db.Column(db.String(255), unique=True, nullable=False)
	price=db.Column(db.Integer, nullable=True)
	image=db.Column(db.String(255))
	description=db.Column(db.String(255))
	
	def __repr__(self):
		return '<book{self.id} {self.name}>'
	def seralize(self):
		return{ 
		'id': self.id,
		'name':self.name,
		'slug':self.slug,
		'price':self.price,
		'image':self.image,
		'desciption':self.description,
		}	 
	
