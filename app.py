from flask import Flask,jsonify
import pymysql
from Resources.registration import UserRegistration
from Resources.login import UserLogin, BuyorSell, Users
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['PREFERRED_URL_SCHEME']='https'
app.config['JWT_SECRET_KEY']='allrounder'
api = Api(app)
jwt = JWTManager(app)

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error': 'authorization_required',
        "description": "Request does not contain an access token."
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'invalid_token',
        'message': 'Signature verification failed.'
    }), 401


api.add_resource(UserRegistration,'/reg')
api.add_resource(UserLogin,'/login')
api.add_resource(BuyorSell,'/bs')
api.add_resource(Users,'/users')


#UserLogin, BuyorSell, Users

if __name__=='__main__':
    app.run(debug=True)
