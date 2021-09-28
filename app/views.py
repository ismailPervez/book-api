# the routes and view functions
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
    def get(self, book_id):
        # user must be logged in to see the books he/she has
        return jsonify({"status": "ok", "data": books[book_id - 1]})

    def post(self):
        # this will be posted with the user id
        args = book_args.parse_args()
        bookId = len(books) + 1
        args.id = bookId
        books.append(args)
        return jsonify({"status": "ok", "message": "data added"})


api.add_resource(Book, '/book', '/book/<int:book_id>')