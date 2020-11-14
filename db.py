from flask import jsonify
from decimal import Decimal
import pymysql
import base64
#import datetime

"""args_tuple is used to avoid syntax errors while inserting BLOB data. A tuple of arguments is sent to the 
keyword argument 'args_tuple'. If args_tuple is not None, the query function is given 
the tuple of arguments to use in the query which is a format string.
return_json is True by default , if set to false it returns a list of dictionaries for debugging"""

#deafult_host = '127.0.0.1'
#default_user = 'root'
#default_password = ''
#default_db = 'agrotrades'

def query(querystr, args_tuple=None, return_json=True):
    connection=pymysql.connect( host = '127.0.0.1',
                                user = 'root',
                                password = '',
                                db = 'agrotrades',
                                cursorclass = pymysql.cursors.DictCursor )
    
    connection.begin()
    cursor=connection.cursor()
    
    if args_tuple:
        cursor.execute(querystr,args_tuple)
    else:
        cursor.execute(querystr)
    
    result=encode(cursor.fetchall())
    connection.commit()
    cursor.close()
    connection.close()
    if return_json:
         return jsonify(result)
    else:
        return result

def getBase64Str(value):
    return base64.b64encode(value).decode('utf-8')


# encode function converts decimals to strings 
# and also converts BLOB files 
# which are in 'bytes' datatype to a base64 encoded string

# encode time and date values so that they are 
# readable and user friendly
def encode(data):
    #iterate through rows
    for row in data:
        for key, value in row.items():
            if isinstance(value, Decimal):
                row[key] = str(value)
            elif isinstance(value, bytes):
                row[key] = getBase64Str(value)
            '''elif isinstance(value,datetime.timedelta):
                row[key] = str(value)
            elif isinstance(value,datetime.date):
                row[key] = str(value)'''
                
    return data
