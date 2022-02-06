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
            'DRIVER={FreeTDS};SERVER=10.29.112.3;PORT=1433;DATABASE=firstdb;UID=sqlserver;PWD=Giulio2022', autocommit=False)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')