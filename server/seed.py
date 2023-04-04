from app import app
from models import db, User, Card, Game

with app.app_context():


    print('creating users')
    users = [
        {'username': 'alice', 'password': 'password1'},
        {'username': 'bob', 'password': 'password2'},
        {'username': 'charlie', 'password': 'password3'},
        {'username': 'dave', 'password': 'password4'},
        {'username': 'eve', 'password': 'password5'},
    ]
    for user in users:
        new_user = User(username=user['username'], _password_hash=user['password'])
        db.session.add(new_user)



    print('creating cards')
    suits = ['H', 'D', 'C', 'S']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    # Seed the cards table with a standard deck of playing cards
    for suit in suits:
        for value in values:
            card = Card(value=value, suit=suit)
            db.session.add(card)



    print('creating games')
    games = [
        {'name': 'Game 1', 'user_id': 1, 'result': 'Win', 'card_id':[1,11], 'user_hand':'','dealer_hand':''},
        # {'name': 'Game 2', 'user_id': 2, 'result': 'Loss', 'card_id':[5,10,11]},
        # {'name': 'Game 3', 'user_id': 3, 'result': 'Tie', 'card_id':[1,10]},
        # {'name': 'Game 4', 'user_id': 4, 'result': 'Win'},
        # {'name': 'Game 5', 'user_id': 5, 'result': 'Loss'},
    ]
    for game in games:
        new_game = Game(name=game['name'], user_id=game['user_id'], result=game['result'], user_hand=game['user_hand'],dealer_hand=game['dealer_hand'])
        db.session.add(new_game)


    db.session.commit()
    print("Complete.")