from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query

class UserRegistration(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('full_name',type=str,required=True,help="Full Name cannot be  blank!")
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('state',type=str,required=True,help="State cannot be  blank!")
        parser.add_argument('password',type=str,required=True,help="Password cannot be  blank!")
        parser.add_argument('phno',type=str,required=True,help="Phone Number cannot be  blank!")
        parser.add_argument('location',type=str,required=True,help="Phone Number cannot be  blank!")
        data= parser.parse_args()
        #try:
        x=query(f"""SELECT * FROM agrotrades.user_details WHERE email='{data['email']}'""",return_json=False)
        if len(x)>0: return {"message":"A registration with that Email ID already exists."}
        #except:
        #return {"message":"There was an error inserting into table."}
        #if(data['Previous_office']!=None and data['previous_position']!=None and data['years_of_service']!=None):
        #try:
        query(f"""INSERT INTO agrotrades.user_details VALUES('{data['full_name']}',
                                                                 '{data['email']}',
                                                                 '{data['state']}',
                                                                 '{data['password']}',
                                                                 '{data['phno']}',
                                                                  NULL,
                                                                 '{data['location']}')""")
        #except:
            #return {"message":"There was an error inserting into table."},400
        #return {"message":"Successfully Inserted."}