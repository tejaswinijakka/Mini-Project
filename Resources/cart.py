#SUCCESSFULLY TESTED
#This page is for the purchaser to see what all he placed in the cart
#Displays the items present in a buyer's cart.

from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query
import base64

class MyCCart(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email Id Cannot be blank')
        #parser.add_argument('cart_id', type=str, required=True, help='Cart Id Cannot be blank')
        data = parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(cid) FROM agrotrades.cart WHERE email='{data["email"]}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(cid)']>=1):
                return query(f"""SELECT c.cid, item_name from agrotrades.cart c inner join agrotrades.commercial co on c.cid = co.cid  WHERE c.email = '{data['email']}'""")
            else:
                return {"message":"You have not made any purchases in the commercial section"}
        except:
            return {"message":"Error connecting to tables"}

class MyDCart(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email Id Cannot be blank')
        data = parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(did) FROM agrotrades.cart WHERE email='{data["email"]}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(did)']>=1):
                return query(f"""SELECT c.did, item_named from agrotrades.cart c inner join agrotrades.dairy d on c.did = d.did  WHERE c.email = '{data['email']}'""")
            else:
                return {"message":"You have not made any purchases in the Dairy section"}
        except:
            return {"message":"Error connecting to tables"}

class MyGCart(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email Id Cannot be blank')
        data = parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(gid) FROM agrotrades.cart WHERE email='{data["email"]}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(gid)']>=1):
                return query(f"""SELECT c.gid, item_nameg from agrotrades.cart c inner join agrotrades.grains g on c.gid = g.gid  WHERE c.email = '{data['email']}'""")
            else:
                return {"message":"You have not made any purchases in the Grains section"}
        except:
            return {"message":"Error connecting to tables"}

class MyVCart(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email Id Cannot be blank')
        data = parser.parse_args()
        try:
            s=query(f"""SELECT COUNT(vid) FROM agrotrades.cart WHERE email='{data["email"]}'""",return_json=False)
            print(s)
            if(s[0]['COUNT(vid)']>=1):
                return query(f"""SELECT c.vid, item_namev from agrotrades.cart c inner join agrotrades.vegfruits v on c.vid = v.vid  WHERE c.email = '{data['email']}'""")
            else:
                return {"message":"You have not made any purchases in the Vegetable and fruit section"}
        except:
            return {"message":"Error connecting to tables"}