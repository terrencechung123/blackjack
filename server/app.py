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


class GetUserByID(Resource):
    def get(self, id):
        try:
            id = str(id)
            user = User.query.filter_by(id=id).first()
            return make_response(user.to_dict(rules=('posts',)), 200)
        except:
            abort(404, "User not found")

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
api.add_resource(GetUserByID, '/users/<int:id>')

class UpdateGame(Resource):
    def post(self):
        user_id = request.form['user_id']
        card_id = request.form['card_id']
        dealer_hand = request.form['dealer_hand']
        user_hand = request.form['user_hand']

        # code to update the game database here
        game = Game(user_id=user_id, card_id=card_id,
                    dealer_hand=dealer_hand, user_hand=user_hand)
        db.session.add(game)
        db.session.commit()
        return {'message': 'Game updated successfully.'}

api.add_resource(UpdateGame, '/api/update_game')

if __name__ == '__main__':
    app.run(debug=True)