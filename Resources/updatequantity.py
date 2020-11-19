#TESTED SUCCESSFULLY
#Used to update the quantities of the produce.

from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query

class UpdateCommercial(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        #parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('cid',type=str,required=True,help="Item ID cannot be  blank!")
        parser.add_argument('quantity',type=int,required=True,help="Quantity cannot be blank!")
        data= parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(quantity) FROM agrotrades.commercial WHERE cid='{data['cid']}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(quantity)']==1):
                query(f"""UPDATE agrotrades.commercial
                            SET quantity = '{data['quantity']}'
                            WHERE cid = '{data['cid']}'""")
            else:
                return{"message":"You have no quantity left"}
        except:
            return {"message":"Error connecting to cart table"}
        return{"message":"successfully inserted/updated"}

class UpdateDairy(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        #parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('did',type=str,required=True,help="Item ID cannot be  blank!")
        parser.add_argument('quantityd',type=int,required=True,help="Quantity cannot be blank!")
        data= parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(quantityd) FROM agrotrades.dairy WHERE did='{data['did']}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(quantityd)']==1):
                query(f"""UPDATE agrotrades.dairy
                            SET quantityd = '{data['quantityd']}'
                            WHERE did = '{data['did']}'""")
            else:
                return{"message":"You have no quantity left"}
        except:
            return {"message":"Error connecting to cart table"}
        return{"message":"successfully inserted/updated"}

class UpdateGrains(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        #parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('gid',type=str,required=True,help="Item ID cannot be  blank!")
        parser.add_argument('quantityg',type=int,required=True,help="Quantity cannot be blank!")
        data= parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(quantityg) FROM agrotrades.grains WHERE gid='{data['gid']}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(quantityg)']==1):
                query(f"""UPDATE agrotrades.grains
                            SET quantityg = '{data['quantityg']}'
                            WHERE gid = '{data['gid']}'""")
            else:
                return{"message":"You have no quantity left"}
        except:
            return {"message":"Error connecting to cart table"}
        return{"message":"successfully inserted/updated"}

class UpdateVegfruits(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        #parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('vid',type=str,required=True,help="Item ID cannot be  blank!")
        parser.add_argument('quantityv',type=int,required=True,help="Quantity cannot be blank!")
        data= parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(quantityv) FROM agrotrades.vegfruits WHERE vid='{data['vid']}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(quantityv)']==1):
                query(f"""UPDATE agrotrades.vegfruits
                            SET quantityv = '{data['quantityv']}'
                            WHERE vid = '{data['vid']}'""")
            else:
                return{"message":"You have no quantity left"}
        except:
            return {"message":"Error connecting to cart table"}
        return{"message":"successfully inserted/updated"}