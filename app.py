from flask import Flask, jsonify, request, Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Open-Saturday!'

# GET books
@app.route('/books')
def get_books():
    return jsonify({'books': books})

# GET books/isbn_number
@app.route('/books/<int:isbn>')
def get_a_book(isbn):
    book = {}
    for item in books:
        if item['isbn'] == isbn:
            book = {
                'name': item['name'],
                'price': item['price']
            }
    return jsonify(book)

def add_book():
    pass

def update_book():
    pass

def replace_book(isbn):
    pass

def delete_book(isbn):
    pass

def validate_book(bookObject):
    pass

books = [
    {
        'name': 'Becoming a World Class Dev',
        'price': 45000,
        'isbn': 12312312
    },
    {
        'name': 'How to excel in Andela Bootcamp',
        'price': 12500,
        'isbn': 123142341
    }
]

app.run(port=5000)
