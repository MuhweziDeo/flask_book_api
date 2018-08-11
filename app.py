from flask import Flask, jsonify, request, Response, json

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

# POST /books
@app.route('/books', methods=['POST'])
def add_book():
    request_data  = request.get_json()
    if (valid_book(request_data)):
        book = {
            'name': request_data['name'],
            'price': request_data['price'],
            'isbn': request_data['isbn']
        }
        books.append(book)
        response = Response("", 201, mimetype="application/json")
        response.headers['Location'] = "books/" + str(request_data['isbn'])
        return response
    else:
        bad_object = {
            "error": "Invalid book object",
            "help_string":
                "Request format should be {'name': 'Tha cat in the hat',"
                "'price': '7.99','isbn': 12319881212 }"
        }
        response = Response(json.dumps(bad_object), status=400, mimetype="appliation/json")
        return response
            

# PATCH /books/isbn_number
@app.route('/books/<int:isbn>', methods=['PATCH'])
def update_book(isbn):
    request_data = request.get_json()
    updated_book = {}

    if ("name" in request_data):
        updated_book["name"] = request_data["name"]
    
    if ("price" in request_data):
        updated_book["price"] = request_data["price"]

    for book in books:
        if book["isbn"] == isbn:
            book.update(updated_book) 
    response = Response("", status="204")
    response.headers['Location'] ="/books" + str(isbn)
    return response

def replace_book(isbn):
    pass

def delete_book(isbn):
    pass

def valid_book(bookObject):
    if "name" in bookObject and "price" in bookObject and "isbn" in bookObject:
        return True
    else:
        return False

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
