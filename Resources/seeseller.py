#This page is for the seller itself to see what all items he uploaded

from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query
import base64

class SeeMyUploadsC(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        data=parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(email) FROM agrotrades.commercial WHERE email='{data["email"]}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(email)']>=1):
                return query(f"""SELECT item_name, quantity, quality, comments, image1, image2, image3, image4, image5 from agrotrades.commercial where email IN'{data['email']}'""")
            else:
                return {"message":"You have not uploaded anything in commercial section"}
        except:
            return {"message":"There was an error connecting to the table"}

class SeeMyUploadsD(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        data=parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(email) FROM agrotrades.dairy WHERE email='{data["email"]}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(email)']>=1):
                return query(f"""SELECT item_named, quantityd, qualityd, commentsd, image1, image2, image3, image4, image5 from agrotrades.dairy where email IN'{data['email']}'""")
            else:
                return {"message":"You have not uploaded anything in dairy section"}
        except:
            return {"message":"There was an error connecting to the table"}

class SeeMyUploadsG(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        data=parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(email) FROM agrotrades.grains WHERE email='{data["email"]}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(email)']>=1):
                return query(f"""SELECT item_nameg, quantityg, qualityg, commentsg, image1, image2, image3, image4, image5 from agrotrades.grains where email IN'{data['email']}'""")
            else:
                return {"message":"You have not uploaded anything in grains section"}
        except:
            return {"message":"There was an error connecting to the table"}

class SeeMyUploadsV(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        data=parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(email) FROM agrotrades.vegfruits WHERE email='{data["email"]}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(email)']>=1):
                return query(f"""SELECT item_namev, quantityv, qualityv, commentsv, image1, image2, image3, image4, image5 from agrotrades.vegfruits where email IN'{data['email']}'""")
            else:
                return {"message":"You have not uploaded anything in Vegetable and Fruits section"}
        except:
            return {"message":"There was an error connecting to the table"}