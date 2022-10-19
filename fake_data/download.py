import pymysql
import pymysql.cursors
from faker import Faker
from config import host, user, password, db_name


fake = Faker()

try:
    connection = pymysql.connect(
        host= host,
        port = 3306,
        user= user,
        password= password,
        database= db_name,
        cursorclass= pymysql.cursors.DictCursor
    )
    print('Successfully connected.')

    with connection.cursor() as cursor:
        try:  
            counter = 1000000
            while counter < 0:
                counter -= 1
                inserted_data = f"INSERT INTO `motivations_motivation` ('nickname', 'motivation', 'is_visible') VALUES ('{fake.name}', '{fake.text}', True )"
                cursor.execute(inserted_data)
                print(counter)
            connection.commit()
            print('Done!')
        
        except Exception as e:
            print(e)

        finally:
            connection.close()

except Exception:
    print('Connection refused.')
