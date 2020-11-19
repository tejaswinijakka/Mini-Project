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
from Resources.deleteinterests import *
from Resources.updatequantity import *
from Resources.deleteseller import *
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
#from flask_ngrok import run_with_ngrok

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

#User Registration
api.add_resource(UserRegistration,'/reg')

#User login
api.add_resource(UserLogin,'/login')

#To check whether a particular user wants to buy or sell
api.add_resource(BuyorSell,'/bs')

#You can say this is 1 useless API(I created it for my reference)
api.add_resource(Users,'/users')

#ALL ENDPOINTS NAME ARE SAME AS CLASS NAME INORDER TO AVOID CONFUSION

#These APIs are present in seller.py file. 
#Farmer uploads data about his produce
api.add_resource(Commercial,'/commercial')                    
api.add_resource(Dairy,'/dairy')          
api.add_resource(Grains,'/grains')
api.add_resource(VegFruits,'/vegfruits')

#These APIs are present in updatequantity.py file.
#Used to update the quantities of the produce.
api.add_resource(UpdateCommercial,'/updatecommercial')
api.add_resource(UpdateDairy,'/updatedairy')
api.add_resource(UpdateGrains,'/updategrains')
api.add_resource(UpdateVegfruits,'/updatevegfruits')

#These APIs are present in deleteseller.py file.
#Used to delete the produce uploaded by the farmer from DB
api.add_resource(DCommercial,'/dcommercial')
api.add_resource(DDairy,'/ddairy')
api.add_resource(DGrains,'/dgrains')
api.add_resource(DVegfruits,'/dvegfruits')

#These APIs are present in seeseller.py file.
#Used to view the produce uploaded by the farmer by himself.
api.add_resource(SeeMyUploadsC,'/seemyuploadsc')
api.add_resource(SeeMyUploadsD,'/seemyuploadsd')
api.add_resource(SeeMyUploadsG,'/seemyuploadsg')
api.add_resource(SeeMyUploadsV,'/seemyuploadsv')

#These APIs present in buyer.py
#Used by buyers to see the produces uploaded by farmers.(1st GET REQUEST)
api.add_resource(SeeCommercial,'/seecommercial')
api.add_resource(SeeDairy,'/seedairy')
api.add_resource(SeeGrains,'/seegrains')
api.add_resource(SeeVegfruits,'/seevegfruits')

#These APIs present in seedetails.py
#Used by buyers to see the produces uploaded by farmers along with farmer details(2nd GET REQUEST)
api.add_resource(SeeCOwnerDetails,'/seecownerdetails')
api.add_resource(SeeDOwnerDetails,'/seedownerdetails')
api.add_resource(SeeGOwnerDetails,'/seegownerdetails')
api.add_resource(SeeVOwnerDetails,'/seevownerdetails')

#These APIs are present in search.py
#APIs for search bar
api.add_resource(SearchCommercial,'/searchcommercial')
api.add_resource(SearchGrains,'/searchgrains')
api.add_resource(SearchDairy,'/searchdairy')
api.add_resource(SearchVegFruits,'/searchvegfruits')

#These APIs are present in postInterests.py
#When buyer presses the interested button for a particular item,
#that item ID will be uploaded into the cart table
api.add_resource(CommercialInterest,'/commercialinterest')
api.add_resource(DairyInterest,'/dairyinterest')
api.add_resource(GrainsInterest,'/grainsinterest')
api.add_resource(VegFruitsInterest,'/vegfruitsinterest')

#These APIs are present in cart.py
#Displays the items present in a buyer's cart.
api.add_resource(MyCCart,'/myccart')
api.add_resource(MyDCart,'/mydcart')
api.add_resource(MyGCart,'/mygcart')
api.add_resource(MyVCart,'/myvcart')

#These APIs are present in deleteinterests.py
#Used to remove items from the cart.
api.add_resource(DCommercialInterest,'/dcommercialinterest')
api.add_resource(DDairyInterest,'/ddairyinterest')
api.add_resource(DGrainsInterest,'/dgrainsinterest')
api.add_resource(DVegFruitsInterest,'/dvegfruitsinterest')


if __name__=='__main__':
    app.run()
