#TESTED SUCCESSFULLY
#Used to remove items from the cart.

from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query

class DCommercialInterest(Resource):
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
                x=query(f"""SELECT COUNT(cid)FROM agrotrades.cart WHERE cid='{data['cid']}' AND
                                                                        email='{data['email']}'""",return_json=False)
                print(x)
                if(x[0]['COUNT(cid)']==1):
                    query(f"""DELETE FROM agrotrades.cart
                              WHERE cid = '{data['cid']}'
                              AND email = '{data['email']}'""")
                    #query(f"""UPDATE agrotrades.cart
                                #SET cid = NULL
                                #WHERE email = '{data['email']}'
                                #AND cid = '{data['cid']}'""")
                else:
                    return{"message":"You did not add item into your cart list"}
            else:
                #query(f"""INSERT INTO agrotrades.cart(email,cid) 
                                                        #VALUES('{data['email']}',
                                                                #'{data['cid']}')""")
                return{"message":"You did not add item into your cart list email"}
        except:
            return {"message":"Error connecting to cart table"}
        return{"message":"successfully deleted/updated"}

class DDairyInterest(Resource):
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
                x=query(f"""SELECT COUNT(did)FROM agrotrades.cart WHERE did='{data['did']}' AND
                                                                        email='{data['email']}'""",return_json=False)
                print(x)
                if(x[0]['COUNT(did)']==1):
                    query(f"""DELETE FROM agrotrades.cart
                              WHERE did = '{data['did']}'
                              AND email = '{data['email']}'""")
                    '''query(f"""UPDATE agrotrades.cart
                                SET did = NULL
                                WHERE email = '{data['email']}'
                                AND did = '{data['did']}'""")'''
                else:
                    return{"message":"You did not add item into your cart list"}
            else:
                #query(f"""INSERT INTO agrotrades.cart(email,cid) 
                                                        #VALUES('{data['email']}',
                                                                #'{data['cid']}')""")
                return{"message":"You did not add item into your cart list email"}
        except:
            return {"message":"Error connecting to cart table"}
        return{"message":"successfully deleted/updated"}

class DGrainsInterest(Resource):
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
                x=query(f"""SELECT COUNT(gid)FROM agrotrades.cart WHERE gid='{data['gid']}' AND
                                                                        email='{data['email']}'""",return_json=False)
                print(x)
                if(x[0]['COUNT(gid)']==1):
                    query(f"""DELETE FROM agrotrades.cart
                              WHERE gid = '{data['gid']}'
                              AND email = '{data['email']}'""")
                    '''query(f"""UPDATE agrotrades.cart
                                SET gid = NULL
                                WHERE email = '{data['email']}'
                                AND gid = '{data['gid']}'""")'''
                else:
                    return{"message":"You did not add item into your cart list"}
            else:
                #query(f"""INSERT INTO agrotrades.cart(email,cid) 
                                                        #VALUES('{data['email']}',
                                                                #'{data['cid']}')""")
                return{"message":"You did not add item into your cart list email"}
        except:
            return {"message":"Error connecting to cart table"}
        return{"message":"successfully deleted/updated"}

class DVegFruitsInterest(Resource):
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
                x=query(f"""SELECT COUNT(vid)FROM agrotrades.cart WHERE vid='{data['vid']}' AND
                                                                        email='{data['email']}'""",return_json=False)
                print(x)
                if(x[0]['COUNT(vid)']==1):
                    query(f"""DELETE FROM agrotrades.cart
                              WHERE vid = '{data['vid']}'
                              AND email = '{data['email']}'""")
                    '''query(f"""UPDATE agrotrades.cart
                                SET vid = NULL
                                WHERE email = '{data['email']}'
                                AND vid = '{data['vid']}'""")'''
                else:
                    return{"message":"You did not add item into your cart list"}
            else:
                #query(f"""INSERT INTO agrotrades.cart(email,cid) 
                                                        #VALUES('{data['email']}',
                                                                #'{data['cid']}')""")
                return{"message":"You did not add item into your cart list email"}
        except:
            return {"message":"Error connecting to cart table"}
        return{"message":"successfully deleted/updated"}