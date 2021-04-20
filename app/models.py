from app import db

class User(db.Model):
    """
    Attributes
    ----------
    id : int
        unique id of an author
    author : str
        name of person who writes a message
    message : string
        a link to the Messages table

    Methods
    -------
    __repr__():
        decides format for when this class is printed
    """

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String, nullable = False, unique = True)

    message = db.relationship('Messages', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
        """
        Decides format for when this class is printed
        """
        return '{}'.format(self.author)
    #        return f'<User {self.author}>'

class Messages(db.Model):
    """
    Attributes
    ----------
    id : int
        id for a message
    message : string
        message that a user types
    user_id : int
        link to id in User class. Id of the user who types a message

    Methods
    -------
    __repr__():
        decides format for when this class is printed
    """
    id = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.String, nullable = False, unique = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr(self):
        """
        Decides format for when this class is printed
        """
        return '<{}>'.format(self.body)
    #        return '<Message: {}>'.format(self.body)
