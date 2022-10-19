import pymysql
import pymysql.cursors
from pymongo import MongoClient
import config


#Connect to Mongo database and download data to this database.
 
def mongo_connect(res):

    client = MongoClient(f"mongodb://{config.mongo_host}:{config.mongo_port}/")
    db = client[config.mongo_db]
    
    motivation = {
            "_id": list(db.motivations.find().sort('_id', -1).limit(1))[0]['_id'] + 1,
            "nickname": res["nickname"],
            "motivation": res["motivation"],
            "is_visible": True
    }
    
    db.motivations.insert_one(motivation)






#Connect to MySQL database and upload data fom this database.

try:
    connection = pymysql.connect(
        host= config.sql_host,
        port = 3306,
        user= config.sql_user,
        password= config.sql_password,
        database= config.sql_db_name,
        cursorclass= pymysql.cursors.DictCursor
    )
    print('Successfully connected to MySQL database.')
    with connection.cursor() as cursor:
        try:  
            select_data = 'SELECT nickname, motivation FROM `motivations_motivation`'
            cursor.execute(select_data)
            result = cursor.fetchall()
            for res in result:
                mongo_connect(res)

        except Exception as ex:
            print(ex)

        finally:
            connection.close()

except Exception:
    print('Connection refused.')


print('Done!')
