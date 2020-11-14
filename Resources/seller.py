from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from flask import jsonify
from db import query
import base64

'''def convertToBase64(value):
    return base64.b64encode(value.encode())'''

class Commercial(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('item_name',type=str,required=True,help="Item Name cannot be  blank!")
        parser.add_argument('quantity',type=int,required=True,help="Quantity cannot be  blank!")
        parser.add_argument('quality',type=str,required=True,help="Quality cannot be  blank!")
        parser.add_argument('comments',type=str,required=True,help="comments cannot be  blank!")
        #parser.add_argument('rating',type=int,required=True,help="Rating cannot be  blank!")
        parser.add_argument('image1',type=str,required=True,help="image1 cannot be  blank!")
        parser.add_argument('image2',type=str,required=True,help="image2 cannot be  blank!")
        parser.add_argument('image3',type=str,required=True,help="image3 cannot be  blank!")
        parser.add_argument('image4',type=str,required=True,help="image4 cannot be  blank!")
        parser.add_argument('image5',type=str,required=True,help="image5 cannot be  blank!")
        data = parser.parse_args()
        #if data['quality']!=None and data['comments']!=None and data['rating']!=None and data['image1']!=None and data['image2']!=None and data['image3']!=None and data['image4']!=None and data['image5']!=None :
        try:
            query(f"""INSERT INTO agrotrades.commercial VALUES({data['email']},
                                                                '{data['item_name']}',
                                                                {data['quantity']},
                                                                '{data['quality']}',
                                                                '{data['comments']}',
                                                            
                                                                '{data['image1']}',
                                                                '{data['image2']}',
                                                                '{data['image3']}',
                                                                '{data['image4']}',
                                                                '{data['image5']}')""")
        except:
            return {"message":"There was an error inserting into commercial table."},500
        return {"message":"Successfully Inserted."},201

class Dairy(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('item_named',type=str,required=True,help="Item Name cannot be  blank!")
        parser.add_argument('quantityd',type=int,required=True,help="Quantity cannot be  blank!")
        parser.add_argument('qualityd',type=str,required=True,help="Quality cannot be  blank!")
        parser.add_argument('commentsd',type=str,required=True,help="comments cannot be  blank!")
        #parser.add_argument('ratingd',type=int,required=True,help="Rating cannot be  blank!")
        parser.add_argument('image1',type=str,required=True,help="image1 cannot be  blank!")
        parser.add_argument('image2',type=str,required=True,help="image2 cannot be  blank!")
        parser.add_argument('image3',type=str,required=True,help="image3 cannot be  blank!")
        parser.add_argument('image4',type=str,required=True,help="image4 cannot be  blank!")
        parser.add_argument('image5',type=str,required=True,help="image5 cannot be  blank!")
        data = parser.parse_args()
        #if data['quality']!=None and data['comments']!=None and data['rating']!=None and data['image1']!=None and data['image2']!=None and data['image3']!=None and data['image4']!=None and data['image5']!=None :
        try:
            query(f"""INSERT INTO agrotrades.dairy VALUES({data['email']},
                                                                '{data['item_named']}',
                                                                {data['quantityd']},
                                                                '{data['qualityd']}',
                                                                '{data['commentsd']}',
                                                                
                                                                '{data['image1']}',
                                                                '{data['image2']}',
                                                                '{data['image3']}',
                                                                '{data['image4']}',
                                                                '{data['image5']}')""")
        except:
            return {"message":"There was an error inserting into dairy table."},500
        return {"message":"Successfully Inserted."},201

class Grains(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('item_nameg',type=str,required=True,help="Item Name cannot be  blank!")
        parser.add_argument('quantityg',type=int,required=True,help="Quantity cannot be  blank!")
        parser.add_argument('qualityg',type=str,required=True,help="Quality cannot be  blank!")
        parser.add_argument('commentsg',type=str,required=True,help="comments cannot be  blank!")
        #parser.add_argument('ratingg',type=int,required=True,help="Rating cannot be  blank!")
        parser.add_argument('image1',type=str,required=True,help="image1 cannot be  blank!")
        parser.add_argument('image2',type=str,required=True,help="image2 cannot be  blank!")
        parser.add_argument('image3',type=str,required=True,help="image3 cannot be  blank!")
        parser.add_argument('image4',type=str,required=True,help="image4 cannot be  blank!")
        parser.add_argument('image5',type=str,required=True,help="image5 cannot be  blank!")
        data = parser.parse_args()
        #if data['quality']!=None and data['comments']!=None and data['rating']!=None and data['image1']!=None and data['image2']!=None and data['image3']!=None and data['image4']!=None and data['image5']!=None :
        try:
            query(f"""INSERT INTO agrotrades.grains VALUES({data['email']},
                                                                '{data['item_nameg']}',
                                                                {data['quantityg']},
                                                                '{data['qualityg']}',
                                                                '{data['commentsg']}',
                                                                
                                                                '{data['image1']}',
                                                                '{data['image2']}',
                                                                '{data['image3']}',
                                                                '{data['image4']}',
                                                                '{data['image5']}')""")
        except:
            return {"message":"There was an error inserting into grains table."},500
        return {"message":"Successfully Inserted."},201

class VegFruits(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="Email ID cannot be  blank!")
        parser.add_argument('item_namev',type=str,required=True,help="Item Name cannot be  blank!")
        parser.add_argument('quantityv',type=int,required=True,help="Quantity cannot be  blank!")
        parser.add_argument('qualityv',type=str,required=True,help="Quality cannot be  blank!")
        parser.add_argument('commentsv',type=str,required=True,help="comments cannot be  blank!")
        #parser.add_argument('ratingv',type=int,required=True,help="Rating cannot be  blank!")
        parser.add_argument('image1',type=str,required=True,help="image1 cannot be  blank!")
        parser.add_argument('image2',type=str,required=True,help="image2 cannot be  blank!")
        parser.add_argument('image3',type=str,required=True,help="image3 cannot be  blank!")
        parser.add_argument('image4',type=str,required=True,help="image4 cannot be  blank!")
        parser.add_argument('image5',type=str,required=True,help="image5 cannot be  blank!")
        data = parser.parse_args()
        #if data['quality']!=None and data['comments']!=None and data['rating']!=None and data['image1']!=None and data['image2']!=None and data['image3']!=None and data['image4']!=None and data['image5']!=None :
        try:
            query(f"""INSERT INTO agrotrades.dairy VALUES({data['email']},
                                                                '{data['item_namev']}',
                                                                {data['quantityv']},
                                                                '{data['qualityv']}',
                                                                '{data['commentsv']}',
                                                                
                                                                '{data['image1']}',
                                                                '{data['image2']}',
                                                                '{data['image3']}',
                                                                '{data['image4']}',
                                                                '{data['image5']}')""")
        except:
            return {"message":"There was an error inserting into vegfruits table."},500
        return {"message":"Successfully Inserted."},201