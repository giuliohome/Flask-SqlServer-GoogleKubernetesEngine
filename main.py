import os
from flask import Flask
import pyodbc

app = Flask(__name__)

appversion = 'v.2.0.0 - Cloud Run from Github CI/CD'
@app.route("/version")
def webversion():
    return appversion 

@app.route("/")
def home():
    return "hello from Google Cloud Run with continuous deployment" # CI/CD trigger

@app.route("/setup")
def sqlconnect():

    print("About to conn")
    #Add your own SQL Server IP address, PORT, UID, PWD and Database
    conn = pyodbc.connect(
            'DRIVER={FreeTDS};SERVER=' + os.environ['DB_HOST'] + ';PORT=1433;DATABASE=master;UID=' + os.environ['DB_USERNAME'] +  ';PWD=' + os.environ['DB_PASSWORD'] , autocommit=False)
    # Creating Cursor    
    conn.timeout = 30

    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE appdb.dbo.products (
                product_id int primary key,
                product_name nvarchar(50),
                price int
                )
                ''')

    conn.commit()

    cursor.execute('''
            INSERT INTO  appdb.dbo.products(product_id, product_name, price)
            VALUES
                (1,'Desktop Computer',800),
                (2,'Laptop',1200),
                (3,'Tablet',200),
                (4,'Monitor',350),
                (5,'Printer',150)
                    ''')
    conn.commit()

    #This is just an example

    print('Should have inserted the rows above')
    cursor.close()
    conn.close()
    return "SQL setup/migration finished"

@app.route("/sql")
def test_sql():
    # creating connection Object which will contain SQL Server Connection    
    connection = pyodbc.connect(
            'DRIVER={FreeTDS};SERVER=' + os.environ['DB_HOST'] + ';PORT=1433;DATABASE=master;UID=' + os.environ['DB_USERNAME'] +  ';PWD=' + os.environ['DB_PASSWORD'] , autocommit=False)
    # Creating Cursor    
    connection.timeout = 30
    cursor = connection.cursor()    
    cursor.execute("SELECT * FROM appdb.dbo.products")    
    s = "<table style='border:1px solid red'>"    
    for row in cursor.fetchall():    
        s = s + "<tr>"    
        for x in row:    
            s = s + "<td>" + str(x) + "</td>"    
        s = s + "</tr>"    
    connection.close()    
    return "<html><body>" + s + "</body></html>"  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
