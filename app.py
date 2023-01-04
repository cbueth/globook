from importlib.resources import Resource

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Initialize the app
app = Flask(__name__)
CORS(app)  # Adds support for Cross Origin Resource Sharing (CORS)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)


# Define the database models as explained in the Terminology section of the README
class Author(db.model):
    """Model for author table.

    Attributes:
        id (int, primary key): Primary key for the author table.
        last_name (str, required, > 0): Author's last name.
        first_name (str, required, > 0): Author's first name.
    """
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        """Returns a string representation of the author object."""
        return f"Author('{self.last_name}', '{self.first_name}')"

    # def to_dict(self):
    #     """Returns a dictionary representation of the author object."""
    #     return {
    #         "id": self.id,
    #         "last_name": self.last_name,
    #         "first_name": self.first_name
    #     }


class Book(db.Model):
    """Book model.

    Attributes:
        id (int, primary key): The book's id.
        title (str, required, > 1 character): The book's title.
        author_id (int, foreign key, required): The book's author id.
        author (Author): The book's author.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author = db.relationship('Author', backref=db.backref('books', lazy=True))

    def __repr__(self):
        """Returns a string representation of the book object."""
        return f"Book('{self.title}', '{self.author.last_name}', '{self.author.first_name}')"


class Copy(db.Model):
    """Copy model.

    Travelling copy of a book. Has been donated into the world.

    Attributes:
        uid (str, primary key): The copy's unique identifier.
        book_id (int, foreign key, required): The id of the book that the copy is of.
        book (Book): The copy's book.
        author (Author): The copy's book's author.
        secret (str, required, > 4 character): The copy's secret.
    """
    uid = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    book = db.relationship('Book', backref=db.backref('copies', lazy=True))
    author = db.relationship('Author', backref=db.backref('copies', lazy=True))
    secret = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        """Returns a string representation of the copy object."""
        return f"Copy('{self.uid}', '{self.book.title}', '{self.book.author.last_name}')"


class Catch(db.Model):
    """Catch model.

    A catch is a record of a copy being caught by a user.
    It combines the information of the copy, location, date, and message.
    Latitude and longitude are stored as floats and represented in the Leaflet
    projection default (EPSG:3857).

    Attributes:
        id (int, primary key): The location's id.
        copy_uid (str, foreign key, required): The copy's unique identifier.
        copy (Copy): The copy that was caught.
        author (Author): The copy's book's author.
        book (Book): The copy's book.
        lat (float, required): The location's latitude. In EPSG:3857.
        lon (float, required): The location's longitude. In EPSG:3857.
        uncertainty (float, required): The location's uncertainty.
        date (datetime, required): The date and time that the copy was caught.
        message (str): The message that the user left for the copy.
    """
    id = db.Column(db.Integer, primary_key=True)
    copy_uid = db.Column(db.Integer, db.ForeignKey('copy.uid'), nullable=False)
    copy = db.relationship('Copy', backref=db.backref('catches', lazy=True))
    author = db.relationship('Author', backref=db.backref('catches', lazy=True))
    book = db.relationship('Book', backref=db.backref('catches', lazy=True))
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    uncertainty = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        """Returns a string representation of the catch object."""
        return f"Catch('{self.id}', '{self.date}', '{self.copy.book.title}', '{self.copy.book.author.last_name}')"


class CatchList(Resource):
    """Resource for the catch list.

    Attributes:
        get (function): Returns a list of catches.
    """

    def get(self):
        """Returns a list of catches."""
        catches = Catch.query.all()
        return [
            {
                'id': catch.id,
                'title': catch.book.title,
                'author_last_name': catch.author.last_name,
                'author_first_name': catch.author.first_name,
                'date': catch.date,
                'lat': catch.lat,
                'lon': catch.lon,
                'uncertainty': catch.uncertainty,
                'message': catch.message
            }
            for catch in catches
        ]

api.add_resource(CatchList, '/catches')

@app.route('/')
def index():
    return render_template('index.html')