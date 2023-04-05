from flask import Flask, request, make_response, session, jsonify, abort
from flask_restful import Resource, reqparse, Api, fields, marshal_with
from werkzeug.exceptions import NotFound, Unauthorized


from config import app, db, api
from models import User, Card, Game



class Signup(Resource):
    def post(self):
        data = request.get_json()
        user = User(username=data['username'])
        user.password_hash = data['password']
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        return make_response(user.to_dict(), 201)
api.add_resource(Signup, '/signup')



class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user:
            if user.authenticate(data['password']):
                session['user_id'] = user.id
                return make_response(user.to_dict(), 200)
            else:
                abort(404, 'Login incorrect.')
        else:
            abort(404, 'Login incorrect.')
api.add_resource(Login, '/login')



class AuthorizedSession(Resource):
    def get(self):
        try:
            user = User.query.filter_by(id=session['user_id']).first()
            return make_response(user.to_dict(), 200)
        except:
            abort(401, "Unauthorized")
api.add_resource(AuthorizedSession, '/authorized')



class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return make_response('', 204)
api.add_resource(Logout, '/logout')




class Games(Resource):
    def get(self):
        games = Game.query.all()
        games_dict_list = [game.to_dict()
                                for game in games]
        response = make_response(
            games_dict_list,
            200
        )
        return response
    def post(self):
        data =request.get_json()
        game = Game(
            price = data['price'],
            # card - data["card"],
            card_id = data['card_id'],
            #user = data["user"],
            user_id = data["user_id"]
        )
        db.session.add(game)
        db.session.commit()
        return make_response(game.to_dict(),201)
api.add_resource(Games, '/games')



class GameById(Resource):
    def get(self, id):
        game = Game.query.filter_by(id=id).first()
        if not game:
            return make_response({
                "error": "Game not found"
            }, 404)
        game_dict = game.to_dict(
            rules=('card',))
        response = make_response(game_dict, 200)
        return response
api.add_resource(GameById, '/games/<int:id>')



class Users(Resource):
    def get(self):
        users = User.query.all()
        users_dict_list = [user.to_dict()
                                for user in users]
        response = make_response(
            users_dict_list,
            200
        )
        return response
api.add_resource(Users, "/users")



class UserById(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first().to_dict()
        return make_response(
            user,
            200)
    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        data = request.get_json()
        if not user:
            raise NotFound
        for attr in data:
            setattr(user, attr, data[attr])
        db.session.add(user)
        db.session.commit()
        response = make_response(user.to_dict(), 200)
        return response
api.add_resource(UserById, "/users/<int:id>")



class Cards(Resource):
    def get(self):
        cards = Card.query.all()
        cards_dict_list = [card.to_dict()
                                for card in cards]
        response = make_response(
            cards_dict_list,
            200
        )
        return response
api.add_resource(Cards,"/cards")



class CardById(Resource):
    def get(self, id):
        card = Card.query.filter_by(id=id).first().to_dict()
        return make_response(
            card,
            200)
    def delete(self, id):
        card = Card.query.filter_by(id=id).first()
        if not card:
            return make_response({
                "error": "Card not found"
            }, 404)
        db.session.delete(card)
        db.session.commit()
        return make_response({}, 204)
api.add_resource(CardById, "/cards/<int:id>")



if __name__ == '__main__':
    app.run(debug=True)