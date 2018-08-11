from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Open-Saturday!'

def get_books():
    pass

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

app.run(port=5000)
