#First get request by purchaser

from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query
import base64

class SeeCommercial(Resource):
    @jwt_required
    def get(self):
        '''parser=reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email Id Cannot be blank')
        data = parser.parse_args()'''
        try:
            return query(f"""SELECT c.email, item_name as 'ITEM', quantity as 'QUANTITY', image1 as 'IMAGE1', location FROM agrotrades.commercial c INNER JOIN agrotrades.user_details u on c.email = u.email""")
        except:
            return{"message":"There was an error connecting to commercial table"}

class SeeDairy(Resource):
    @jwt_required
    def get(self):
        try:
            return query(f"""SELECT d.email, item_named as 'ITEM', quantityd as 'QUANTITY', image1 as 'IMAGE1', location FROM agrotrades.dairy d INNER JOIN agrotrades.user_details u on d.email = u.email""")
        except:
            return{"message":"There was an error connecting to dairy table"}

class SeeGrains(Resource):
    @jwt_required
    def get(self):
        try:
            return query(f"""SELECT g.email, item_nameg as 'ITEM', quantityg as 'QUANTITY', image1 as 'IMAGE1', location FROM agrotrades.grains g INNER JOIN agrotrades.user_details u on g.email = u.email""")
        except:
            return{"message":"There was an error connecting to grains table"}

class SeeVegfruits(Resource):
    @jwt_required
    def get(self):
        try:
            return query(f"""SELECT v.email, item_namev as 'ITEM', quantityv as 'QUANTITY', image1 as 'IMAGE1', location FROM agrotrades.vegfruits v INNER JOIN agrotrades.user_details u on v.email = u.email""")
        except:
            return{"message":"There was an error connecting to vegfruits table"}

