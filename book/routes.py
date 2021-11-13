from flask import Blueprint, request, jsonify
from models import Book,db
book_blueprint = Blueprint('book_api_routes',__name__,url_prefix='/api/book')

@book_blueprint.route('/test', methods=['GET'])
def test():
	return "Hello"
@book_blueprint.route('/all', methods=['GET'])
def get_all_books():
	all_books = Book.query.all()
	result = [book.seralize() for book in all_books]
	response = {"result":result}
	return jsonify(response)
	
@book_blueprint.route('/create', methods=['POST'])
def create_books():
	try:
		book = Book()
		book.name = request.form['name']
		book.slug = request.form['slug']
		book.image = request.form['image']
		book.price = request.form['price']
		book.description= request.form['desc']
		db.session.add(book)
		db.session.commit()
	
		response = {'message':'Book created','result': book.seralize()}
	except Exception as e:
		print(str(e))
		response = {'message':'Book creation failed'}
	return jsonify(response)
		
@book_blueprint.route('/<slug>', methods=['GET'])
def book_details(slug):
	book = Book.query.filter_by(slug=slug).first()
	
	if book:
		response = {'result':book.seralize()}
	else:
		response = {'message':'No book found'}
	return jsonify(response)
	
@book_blueprint.route('/delete/<slug>', methods=['GET'])
def book_delete(slug):
	book = Book.query.filter_by(slug=slug).first()
	if book:
		db.session.delete(book)
		db.session.commit()
		response = {'result':'Book deleted'}
	else:
		response = {'message':'No book found to delete'}
	return jsonify(response)				

@book_blueprint.route('/edit/<slug>', methods=['GET'])
def edit_books(slug):
	try:
		book = Book.query.filter_by(slug=slug).first()
		book.name = request.form['name']
		book.slug = request.form['slug']
		book.image = request.form['image']
		book.price = request.form['price']
		book.description= request.form['desc']
		db.session.add(book)
		db.session.commit()
	
		response = {'message':'Book edited','result': book.seralize()}
	except Exception as e:
		print(str(e))
		response = {'message':'Book cant be edited'}
	return jsonify(response)
	
