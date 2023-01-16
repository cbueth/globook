from app import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)

    # general info
    title = db.Column(db.String(250))
    author = db.Column(db.String(250))
    message = db.Column(db.Text)
    donor = db.Column(db.String(250))

    # technical columns
    secret = db.Column(db.String(250))
    date_added = db.Column(db.DateTime)

class Catch(db.Model):
    __tablename__ = 'catches'
    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    lon = db.Column(db.Float)
    lat = db.Column(db.Float)
    radius = db.Column(db.Float)
    message = db.Column(db.Text)

    # maybe this should be split in date_received and date_passed_on?
    date_catched = db.Column(db.DateTime)

    book = db.relationship("Book", back_populates = "catches")
