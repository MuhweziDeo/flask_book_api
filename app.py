from flask import Flask, jsonify, request, Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Open-Saturday!'

# GET books
@app.route('/books')
def get_books():
    return jsonify({'books': books})

def get_a_book():
    pass

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
        'name':'Becoming a World Class Dev',
        'price':'45000',
        'isbn':'12312312'
    },
    {
        'name':'How to excel in Andela Bootcamp',
        'price':'12500',
        'isbn':'123142341'
    }
]

app.run(port=5000)
