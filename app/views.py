# the routes and view functions
from flask import json, request
from app import api
from flask_restful import Resource, reqparse
from flask import jsonify

'''
a book can be returned in 2 ways,
1. if the user wants to get all of the books he has stored/saved/created - User class
2. if the user wants to get a specific book - this will use the Book class, but we need to
have a book_id as a parameter
'''

book_args = reqparse.RequestParser() # instantiate the parser
book_args.add_argument("title", type=str, help="title of the books is required!", required=True)
book_args.add_argument("desc", type=str, help="description of the books is required!", required=True)
book_args.add_argument("ratings", type=float, help="ratings of the books is required!", required=True)

books = [
    {
        "id": 1,
        "title": "the flash",
        "desc": "Barry Allen grows up to become a forensic scientist after being adopted by a cop",
        "ratings": 5.0
    },
    {
        "id": 2,
        "title": "super girl",
        "desc": "Coming from another world after being destroyed, she finds out that on earth she is super",
        "ratings": 3.5
    }
]

class Book(Resource):
    def get(self, book_id=None):
        # user must be logged in to see the books he/she has
        if book_id is None:
            return jsonify({'status': 'fail', 'message': 'book_id is required!'})
        return jsonify({"status": "ok", "data": books[book_id - 1]})

    def post(self):
        # this will be posted with the user id
        args = book_args.parse_args()
        bookId = len(books) + 1
        args.id = bookId
        books.append(args)
        return jsonify({"status": "ok", "message": "data added"})

    def put(self, book_id=None):
        # the data should be sent through json format - same as post
        if book_id is None:
            return jsonify({'status': 'fail', 'message': 'book_id is required!'})

        if request.json is None:
            return jsonify({"status": 'fail', "message": 'no json data found!'})

        # else
        # find the book
        book  = books[book_id - 1] # because counting starts at 0
        print(book)
        if "title" in request.json:
            book['title'] = request.json["title"]
        
        if "desc" in request.json:
            book['desc'] = request.json["desc"]

        if "ratings" in request.json:
            book['ratings'] = request.json["ratings"]

        return jsonify({"status": 'ok', 'message': 'book updated successfully!'})



api.add_resource(Book, '/book', '/book/<int:book_id>')