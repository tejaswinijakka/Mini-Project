#TESTED SUCCESSFULLY
#This page is for 2nd get request by buyer to see the details of the uploader
#Used by buyers to see the produces uploaded by farmers along with farmer details(2nd GET REQUEST)

from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query

class SeeCOwnerDetails(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email ID Cannot be blank')
        data = parser.parse_args()
        try:
            return query(f"""SELECT cid,u.email, full_name, location,state, phno, item_name, quantity, quality, comments, image1, image2, image3, image4, image5 from agrotrades.user_details u inner join agrotrades.commercial c on u.email=c.email where u.email='{data['email']}'""")
        except:
            return{"message":"There was an error connecting to tables"}

class SeeDOwnerDetails(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email Id Cannot be blank')
        data = parser.parse_args()
        try:
            return query(f"""SELECT did,u.email, full_name, location,state, phno, item_named, quantityd, qualityd, commentsd, image1, image2, image3, image4, image5 from agrotrades.user_details u inner join agrotrades.dairy d on u.email=d.email where u.email='{data['email']}'""")
        except:
            return{"message":"There was an error connecting to tables"}

class SeeGOwnerDetails(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email Id Cannot be blank')
        data = parser.parse_args()
        try:
            return query(f"""SELECT gid,u.email, full_name, location,state, phno, item_nameg, quantityg, qualityg, commentsg, image1, image2, image3, image4, image5 from agrotrades.user_details u inner join agrotrades.grains g on u.email=g.email where u.email='{data['email']}'""")
        except:
            return{"message":"There was an error connecting to tables"}

class SeeVOwnerDetails(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email Id Cannot be blank')
        data = parser.parse_args()
        try:
            return query(f"""SELECT vid,u.email, full_name, location,state, phno, item_namev, quantityv, qualityv, commentsv, image1, image2, image3, image4, image5 from agrotrades.user_details u inner join agrotrades.vegfruits v on u.email=v.email where u.email='{data['email']}'""")
        except:
            return{"message":"There was an error connecting to tables"}
    