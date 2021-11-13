import requests

from . import BOOK_API_URL


class BookClient:
    

    @staticmethod
    def get_books():
        url='/api/book/all'
        
        response = requests.get(BOOK_API_URL + url)
        return response.json()

    @staticmethod
    def get_book(slug):
        url='/api/book/'
        response = requests.get(BOOK_API_URL + url + slug)
        return response.json()
