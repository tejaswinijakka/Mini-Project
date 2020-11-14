from flask import Flask,jsonify
import pymysql
from Resources.registration import UserRegistration
from Resources.login import UserLogin, BuyorSell, Users
from Resources.seller import Commercial, Dairy, Grains, VegFruits
from Resources.buyer import SeeCommercial, SeeDairy, SeeGrains, SeeVegfruits
from Resources.seedetails import SeeCOwnerDetails,SeeDOwnerDetails,SeeGOwnerDetails,SeeVOwnerDetails
from Resources.search import *
from Resources.seeseller import *
from Resources.postInterests import *
from Resources.cart import *
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
api.add_resource(Commercial,'/commercial')                    
api.add_resource(Dairy,'/dairy')          
api.add_resource(Grains,'/grains')
api.add_resource(VegFruits,'/vegfruits')
api.add_resource(SeeCommercial,'/seecommercial')
api.add_resource(SeeDairy,'/seedairy')
api.add_resource(SeeGrains,'/seedairy')
api.add_resource(SeeVegfruits,'/seevegfruits')
api.add_resource(SeeCOwnerDetails,'/seecownerdetails')
api.add_resource(SeeDOwnerDetails,'/seedownerdetails')
api.add_resource(SeeGOwnerDetails,'/seegownerdetails')
api.add_resource(SeeVOwnerDetails,'/seevownerdetails')
api.add_resource(SearchCommercial,'/searchcommercial')
api.add_resource(SearchGrains,'/searchgrains')
api.add_resource(SearchDairy,'/searchdairy')
api.add_resource(SearchVegFruits,'/searchvegfruits')
api.add_resource(SeeMyUploadsC,'/seemyuploadsc')
api.add_resource(SeeMyUploadsD,'/seemyuploadsd')
api.add_resource(SeeMyUploadsG,'/seemyuploadsg')
api.add_resource(SeeMyUploadsV,'/seemyuploadsv')
api.add_resource(CommercialInterest,'/commercialinterest')
api.add_resource(DairyInterest,'/dairyinterest')
api.add_resource(GrainsInterest,'/grainsinterest')
api.add_resource(VegFruitsInterest,'/vegfruitsinterest')
api.add_resource(MyCCart,'/myccart')
api.add_resource(MyDCart,'/mydcart')
api.add_resource(MyGCart,'/mygcart')
api.add_resource(MyVCart,'/myvcart')


if __name__=='__main__':
    app.run(debug=True)
