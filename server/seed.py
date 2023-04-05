from config import db
from models import User, Card, Game
from app import app

with app.app_context():

    Game.query.delete()
    User.query.delete()
    Card.query.delete()
    # create users
    users = [
        User(username='player1', _password_hash='password1'),
        User(username='player2', _password_hash='password2'),
        User(username='player3', _password_hash='password3'),
        User(username='player4', _password_hash='password4')
    ]
    db.session.add_all(users)
    db.session.commit()

    # create cards
    cards = [
        Card(name='Ace', value=11, suit='H'),
        Card(name='Two', value=2, suit='H'),
        Card(name='Three', value=3, suit='H'),
        Card(name='Four', value=4, suit='H'),
        Card(name='Five', value=5, suit='H'),
        Card(name='Six', value=6, suit='H'),
        Card(name='Seven', value=7, suit='H'),
        Card(name='Eight', value=8, suit='H'),
        Card(name='Nine', value=9, suit='H'),
        Card(name='Ten', value=10, suit='H'),
        Card(name='Jack', value=10, suit='H'),
        Card(name='Queen', value=10, suit='H'),
        Card(name='King', value=10, suit='H'),

        Card(name='Ace', value=11, suit='D'),
        Card(name='Two', value=2, suit='D'),
        Card(name='Three', value=3, suit='D'),
        Card(name='Four', value=4, suit='D'),
        Card(name='Five', value=5, suit='D'),
        Card(name='Six', value=6, suit='D'),
        Card(name='Seven', value=7, suit='D'),
        Card(name='Eight', value=8, suit='D'),
        Card(name='Nine', value=9, suit='D'),
        Card(name='Ten', value=10, suit='D'),
        Card(name='Jack', value=10, suit='D'),
        Card(name='Queen', value=10, suit='D'),
        Card(name='King', value=10, suit='D'),

        Card(name='Ace', value=11, suit='C'),
        Card(name='Two', value=2, suit='C'),
        Card(name='Three', value=3, suit='C'),
        Card(name='Four', value=4, suit='C'),
        Card(name='Five', value=5, suit='C'),
        Card(name='Six', value=6, suit='C'),
        Card(name='Seven', value=7, suit='C'),
        Card(name='Eight', value=8, suit='C'),
        Card(name='Nine', value=9, suit='C'),
        Card(name='Ten', value=10, suit='C'),
        Card(name='Jack', value=10, suit='C'),
        Card(name='Queen', value=10, suit='C'),
        Card(name='King', value=10, suit='C'),

        Card(name='Ace', value=11, suit='S'),
        Card(name='Two', value=2, suit='S'),
        Card(name='Three', value=3, suit='S'),
        Card(name='Four', value=4, suit='S'),
        Card(name='Five', value=5, suit='S'),
        Card(name='Six', value=6, suit='S'),
        Card(name='Seven', value=7, suit='S'),
        Card(name='Eight', value=8, suit='S'),
        Card(name='Nine', value=9, suit='S'),
        Card(name='Ten', value=10, suit='S'),
        Card(name='Jack', value=10, suit='S'),
        Card(name='Queen', value=10, suit='S'),
        Card(name='King', value=10, suit='S'),
    ]
    db.session.add_all(cards)
    db.session.commit()

    # create games
    games = [
        Game(user_id=1, result='Win'),
        Game(user_id=2, result='Loss'),
        Game(user_id=3, result='Tie'),
        Game(user_id=4, result='Win')
    ]
    games[0].card = [cards[0], cards[1], cards[2]]
    games[1].card = [cards[2], cards[3], cards[4]]
    games[2].card = [cards[4], cards[5], cards[6]]
    games[3].card = [cards[6], cards[7], cards[8]]
    db.session.add_all(games)
    db.session.commit()

    print("Database seeded successfully!")