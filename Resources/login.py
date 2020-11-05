from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query

class User():
    def __init__(self,email,password):
        self.email=email
        self.password=password


    @classmethod
    def getUserByEmail(cls,email):
        result=query(f"""SELECT email,password FROM agrotrades.user_details WHERE email='{email}'""",return_json=False)
        if len(result)>0: return User(result[0]["email"],result[0]['password'])
        return None

class UserLogin(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be blank.")
        parser.add_argument('password',type=str,required=True,help="Password cannot be blank.")
        data=parser.parse_args()
        user=User.getUserByEmail(data['email'])
        if user and safe_str_cmp(user.password,data['password']):
            access_token=create_access_token(identity=user.email,expires_delta=False)
            return {'access_token':access_token},200
        return {"message":"Invalid Credentials!"},400

class Users(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email ID Cannot be blank')
        data= parser.parse_args()
        try:
            return query(f"""Select usertype from agrotrades.user_details where email='{data["email"]}'""")
        except:
            return {"message":"There was an error returning the values."},400

class BuyorSell(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('usertype',type=int,required=True,help="Email ID cannot be  blank!")
        data= parser.parse_args()
        try:
            x=query(f"""UPDATE agrotrades.user_details
                        SET usertype = '{data['usertype']}'
                        WHERE email='{data['email']}'""")
        except:
            return{"message":"There was an error updating"},400
        return{"message":"Successfully updated"},201
