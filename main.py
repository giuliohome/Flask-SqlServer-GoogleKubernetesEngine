import os
from flask import Flask
import pyodbc

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"


def sqlconnect():
    print("About to conn")
    #Add your own SQL Server IP address, PORT, UID, PWD and Database
    conn = pyodbc.connect(
            'DRIVER={FreeTDS};SERVER=' + os.environ['DB_HOST'] + ';PORT=1433;DATABASE=firstdb;UID=' + os.environ['DB_USERNAME'] +  ';PWD=' + os.environ['DB_PASSWORD'] , autocommit=False)

    conn.setencoding('utf-8')

    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE products (
                product_id int primary key,
                product_name nvarchar(50),
                price int
                )
                ''')

    conn.commit()

    cursor.execute('''
            INSERT INTO products (product_id, product_name, price)
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

@app.route("/sql")
def test_sql():
    # creating connection Object which will contain SQL Server Connection    
    connection = pyodbc.connect(
            'DRIVER={FreeTDS};SERVER=' + os.environ['DB_HOST'] + ';PORT=1433;DATABASE=firstdb;UID=' + os.environ['DB_USERNAME'] +  ';PWD=' + os.environ['DB_PASSWORD'] , autocommit=False)
    # Creating Cursor    
    connection.timeout = 30
    cursor = connection.cursor()    
    cursor.execute("SELECT * FROM products")    
    s = "<table style='border:1px solid red'>"    
    for row in cursor.fetchall():    
        s = s + "<tr>"    
        for x in row:    
            s = s + "<td>" + str(x) + "</td>"    
        s = s + "</tr>"    
    connection.close()    
    return "<html><body>" + s + "</body></html>"  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
