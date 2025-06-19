import psycopg2
import os
from dotenv import load_dotenv
import uuid
from datetime import datetime


db_name=os.environ.get("db_name")
db_user = os.environ.get("db_user")
db_password =os.environ.get ("db_password")
db_host = os.environ.get("db_host")
db_port = os.environ.get("db_port")
db_schema =os.environ.get("db_schema")


def database_connection():
    connection_string = f"dbname={db_name} user={db_user} password={db_password} host={db_host} port={db_port} schema={db_schema}"
    Create_Connection = psycopg2.connect(connection_string)
    curs = Create_Connection.cursor() 
# this comm for generat a uuid 
    Generator_uuid=str(uuid.uuid4())
# insertqurey=f"insert into {db_schema}.user (uuid,name,phone_number) VALUES  ($,$,$)"
    insertqurey = f"INSERT INTO user (uuid, name, phone_number) VALUES (%s, %s, %s)"
    values=(Generator_uuid,"viki",9500)
    curs.execute(insertqurey,values)
    return (database_connection)

print(database_connection())

def Select_Query():
# 1. Connect to the DB (exclude schema from connection string)
    connect_db = f"dbname={db_name} user={db_user} password={db_password} host={db_host} port={db_port} schema={db_schema}"
    creat_connection = psycopg2.connect(connect_db)
    cursr = creat_connection.cursor()

 # 2. Set search_path to use the correct schema
    cursr.execute(f"SET search_path TO {db_schema};")

 # 3. Run your SELECT query
    SelectQuery = f"SELECTE * FORM db_name; "
    cursr.execute(SelectQuery)

    row = cursr.fetchall()
       
# 4. Print results
    for row in row :
        print(row)

# 5. close connection
    cursr.close()
    creat_connection.close()

    print(Select_Query)



def delet_qurey():
    
    connect_string = f" dbname={db_name} user={db_user} password={db_password} host={db_host} port={db_port} schema={db_schema}"
    conect_db=psycopg2.connect(connect_string)
    cursr = conect_db.cursor()
    
 # 2. Set search_path to use the correct schema
    cursr.execute(f"SET search_path TO {db_schema};")

 # 3. run your delete qurey
    delete_query =  "DELETE FROM user WHERE uuid = %s"
    cursor.execute(delete_query , (uuid_to_delete,))

    conn.commit()
    print("✅ User deleted successfully")

    cursor.close()
    conn.close()


 
  







# # from fastapi import FastAPI
# # import uvicorn

# # app = FastAPI(title="Tetsing")

# # @app.get("/get_api")
# # def Get_api():
# #     return{"status":"200"}









