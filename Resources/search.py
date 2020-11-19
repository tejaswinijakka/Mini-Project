#TESTED SUCCESSFULLY
#APIs for search bar

from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query

class SearchCommercial(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('item_name', type=str, required=True, help='Item Name Cannot be blank')
        data = parser.parse_args()
        try:
            return query(f"""SELECT item_name as 'ITEM', quantity as 'QUANTITY' ,image1 as 'IMAGE 1' FROM agrotrades.commercial WHERE item_name='{data['item_name']}'""")
        except:
            return{"message":"There was an error connecting to tables"}

class SearchGrains(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('item_nameg', type=str, required=True, help='Item Name Cannot be blank')
        data = parser.parse_args()
        try:
            return query(f"""SELECT item_nameg as 'ITEM', quantityg as 'QUANTITY' ,image1 as 'IMAGE 1' FROM agrotrades.grains WHERE item_nameg='{data['item_nameg']}'""")
        except:
            return{"message":"There was an error connecting to tables"}

class SearchDairy(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('item_named', type=str, required=True, help='Item Name Cannot be blank')
        data = parser.parse_args()
        try:
            return query(f"""SELECT item_named as 'ITEM', quantityd as 'QUANTITY' ,image1 as 'IMAGE 1' FROM agrotrades.dairy WHERE item_named='{data['item_named']}'""")
        except:
            return{"message":"There was an error connecting to tables"}

class SearchVegFruits(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('item_namev', type=str, required=True, help='Item Name Cannot be blank')
        data = parser.parse_args()
        try:
            return query(f"""SELECT item_namev as 'ITEM', quantityv as 'QUANTITY' ,image1 as 'IMAGE 1' FROM agrotrades.vegfruits WHERE item_namev='{data['item_namev']}'""")
        except:
            return{"message":"There was an error connecting to tables"}


