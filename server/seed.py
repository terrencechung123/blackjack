from app import app
from models import db, bcrypt, User, Card, Game

with app.app_context():

    print("Deleting all records...")
    Game.query.delete()
    User.query.delete()
    Card.query.delete()

    print('creating users')
    user1 = User(username='Alice')
    user2 = User(username='Bob')



    print('creating cards')
    card1 = Card(value='2', suit='Hearts')
    card2 = Card(value='3', suit='Hearts')
    card3 = Card(value='4', suit='Hearts')



    print('creating games')
    game1 = Game(name='Game 1', user=user1, card=card1)
    game2 = Game(name='Game 2', user=user2, card=card2)
    game3 = Game(name='Game 3', user=user1, card=card3)


    db.session.add_all([user1, user2, card1, card2, card3, game1, game2, game3])
    db.session.commit()