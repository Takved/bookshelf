# bookshelf

Simple app for testing capabilities of JSON REST server with FastAPI and PostgreSQL async db access methods

Starting server:

1. Clone repo.
2. Build: 	$ docker-compose build
3. Start: 	$ docker-compose up
4. Connect to http://localhost:8000/bookshelf/

Endpoints:
1 Get       ->     /                                (displays short message for starting endpoint address)
2 Get       ->     /bookshelf/              (returns list of books, sorted by "deadline" property of book)
3 Post     ->     /bookshelf/               (add book to bookshelf)
4 Delete  ->     /bookshelf/{title}     (remove book with parameter {title} from bookshelf)
5 Patch   ->     /bookshelf/{title}     (mark book with parameter {title} as readed)

To add book to shelf it's necessary to send JSON request with format:
{
  "title": "string",
  "genre": "string",
  "author": "string",
  "deadline": 0,
  "readed": false
}