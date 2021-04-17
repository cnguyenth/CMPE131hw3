from app import db

class User(db.Model):
    # have the following columns
    # id (int)
    # author (string, unique, can't be null)
    # message (linkd to Messages table)

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String, nullable = False, unique = True)

    message = db.relationship('Messages', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
        return f'<User {self.author}>'

class Messages(db.Model):
    # have the following columns
    # id (int)
    # message (string, not unique, can't be null)
    # user_id link to id (int)

    id = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.String, nullable = False, unique = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # write __repr__ that outputs
    # <Message: MESSAGE_GOES_HERE>
    # replace MESSAGE_GOES_HERE with the message

    def __repr(self):
        return '<Message: {}>'.format(self.body)