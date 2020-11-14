from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query

class CommercialInterest(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('cid',type=str,required=True,help="Item ID cannot be  blank!")
        data= parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(email) FROM agrotrades.cart WHERE email='{data["email"]}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(email)']>=1):
                query(f"""UPDATE agrotrades.cart
                          SET cid = '{data['cid']}'
                          WHERE email = '{data['email']}'""")
            else:
                query(f"""INSERT INTO agrotrades.cart VALUES('{data['email']}',
                                                             '{data['cid']}'""")
        except:
            return {"message":"Error connecting to cart table"}

class DairyInterest(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('did',type=str,required=True,help="Item ID cannot be  blank!")
        data= parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(email) FROM agrotrades.cart WHERE email='{data["email"]}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(email)']>=1):
                query(f"""UPDATE agrotrades.cart
                          SET did = '{data['did']}'
                          WHERE email = '{data['email']}'""")
            else:
                query(f"""INSERT INTO agrotrades.cart VALUES('{data['email']}',
                                                             '{data['did']}'""")
        except:
            return {"message":"Error connecting to cart table"}

class GrainsInterest(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('gid',type=str,required=True,help="Item ID cannot be  blank!")
        data= parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(email) FROM agrotrades.cart WHERE email='{data["email"]}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(email)']>=1):
                query(f"""UPDATE agrotrades.cart
                          SET gid = '{data['gid']}'
                          WHERE email = '{data['email']}'""")
            else:
                query(f"""INSERT INTO agrotrades.cart VALUES('{data['email']}',
                                                             '{data['gid']}'""")
        except:
            return {"message":"Error connecting to cart table"}

class VegFruitsInterest(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('vid',type=str,required=True,help="Item ID cannot be  blank!")
        data= parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(email) FROM agrotrades.cart WHERE email='{data["email"]}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(email)']>=1):
                query(f"""UPDATE agrotrades.cart
                          SET vid = '{data['vid']}'
                          WHERE email = '{data['email']}'""")
            else:
                query(f"""INSERT INTO agrotrades.cart VALUES('{data['email']}',
                                                             '{data['vid']}'""")
        except:
            return {"message":"Error connecting to cart table"}