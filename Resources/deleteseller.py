#TESTED SUCCESSFULLY
#Used to delete the produce uploaded by the farmer from DB

from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query

class DCommercial(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('cid',type=int,required=True,help="Item ID cannot be  blank!")
        data= parser.parse_args()
        try:
            query(f"""DELETE FROM agrotrades.commercial WHERE cid={data['cid']}""")
        except:
            return{"message":"Error connecting to tables"}
        return{"message":"Successfully deleted"}

class DDairy(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('did',type=int,required=True,help="Item ID cannot be  blank!")
        data= parser.parse_args()
        try:
            query(f"""DELETE FROM agrotrades.dairy WHERE did={data['did']}""")
        except:
            return{"message":"Error connecting to tables"}
        return{"message":"Successfully deleted"}

class DGrains(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('gid',type=int,required=True,help="Item ID cannot be  blank!")
        data= parser.parse_args()
        try:
            query(f"""DELETE FROM agrotrades.grains WHERE gid={data['gid']}""")
        except:
            return{"message":"Error connecting to tables"}
        return{"message":"Successfully deleted"}

class DVegfruits(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('vid',type=int,required=True,help="Item ID cannot be  blank!")
        data= parser.parse_args()
        try:
            query(f"""DELETE FROM agrotrades.vegfruits WHERE vid={data['vid']}""")
        except:
            return{"message":"Error connecting to tables"}
        return{"message":"Successfully deleted"}


