#TESTED SUCCESSFULLY
#When buyer presses the interested button for a particular item,
#that item ID will be uploaded into the cart table

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
        #parser.add_argument('cart_id',type=int,required=True,help="Email ID cannot be  blank!")
        data= parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(cid) FROM agrotrades.cart WHERE email='{data["email"]}'
                                                                   AND cid='{data['cid']}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(cid)']>=1):
                return{"message":"Item is already placed in your cart"}
            else:
                query(f"""INSERT INTO agrotrades.cart(email,cid) 
                                                        VALUES('{data['email']}',
                                                                '{data['cid']}')""")
        except:
            return {"message":"Error connecting to cart table"}
        return{"message":"successfully inserted/updated"}

class DairyInterest(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('did',type=str,required=True,help="Item ID cannot be  blank!")
        data= parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(did) FROM agrotrades.cart WHERE email='{data["email"]}'
                                                                   AND did='{data['did']}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(did)']>=1):
                return{"message":"Item is already placed in your cart"}
            else:
                query(f"""INSERT INTO agrotrades.cart(email,did) 
                                                      VALUES('{data['email']}',
                                                             '{data['did']}')""")
        except:
            return {"message":"Error connecting to cart table"}
        return{"message":"successfully inserted/updated"}

class GrainsInterest(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('gid',type=str,required=True,help="Item ID cannot be  blank!")
        data= parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(gid) FROM agrotrades.cart WHERE email='{data["email"]}'
                                                                   AND gid='{data['gid']}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(gid)']>=1):
                return{"message":"Item is already placed in your cart"}
            else:
                query(f"""INSERT INTO agrotrades.cart(email,gid) 
                                                      VALUES('{data['email']}',
                                                             '{data['gid']}')""")
        except:
            return {"message":"Error connecting to cart table"}
        return{"message":"successfully inserted/updated"}

class VegFruitsInterest(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('vid',type=str,required=True,help="Item ID cannot be  blank!")
        data= parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(vid) FROM agrotrades.cart WHERE email='{data["email"]}'
                                                                   AND vid='{data['vid']}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(vid)']>=1):
                return{"message":"Item is already placed in your cart"}
            else:
                query(f"""INSERT INTO agrotrades.cart(email,vid) 
                                                      VALUES('{data['email']}',
                                                             '{data['vid']}')""")
        except:
            return {"message":"Error connecting to cart table"}
        return{"message":"successfully inserted/updated"}