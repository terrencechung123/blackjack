from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt
from sqlalchemy.ext.associationproxy import association_proxy


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-_password_hash','-games')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String)

    games = db.relationship('Game', backref='user')
    cards = association_proxy('games', 'card')


    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))


class Game(db.Model, SerializerMixin):
    __tablename__='games'

    serialize_rules = ('-user_id','-card_id')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))
    result = db.Column(db.String)
    user_hand = db.Column(db.String)
    dealer_hand = db.Column(db.String)




class Card(db.Model, SerializerMixin):
    __tablename__ = 'cards'

    serialize_rules = ('-games',)

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    suit = db.Column(db.String)

    games = db.relationship('Game', backref='card')
    users = association_proxy('games', 'user')



