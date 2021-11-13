from flask import Flask, Blueprint, render_template

from api.book_client import BookClient

blueprint = Blueprint('frontend', __name__)


@blueprint.route('/', methods=['GET'])
def index():
    books = BookClient.get_books()
    
    return render_template('index.html', books=books)

@blueprint.route('/book/<slug>', methods=['GET'])    
def book_details(slug):
	response=BookClient.get_book(slug)
	book=response['result']    
	return render_template('book_details.html', book=book)
