import os
from flask import Flask
import psycopg2
import bucket
from google.cloud import firestore

# The `project` parameter is optional and represents which project the client
# will act on behalf of. If not supplied, the client falls back to the default
# project inferred from the environment.
db = firestore.Client(project='mypulumi')

app = Flask(__name__)

@app.route("/version")
def webversion():
    appVersion = "gunicorn + postgres db on Kubernetes" # bucket.download_blob_as_string("mycloud_bucket", "version.txt")
    return appVersion

@app.route("/")
def home():
    return "Flask gunicorn. Instead of K8s, Google Cloud Run with continuous deployment from Github!!!" # CI/CD trigger

@app.route("/setdata")
def nosqlconnect():
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })
    doc_ref = db.collection(u'users').document(u'aturing')
    doc_ref.set({
        u'first': u'Alan',
        u'middle': u'Mathison',
        u'last': u'Turing',
        u'born': 1912
    })
    return "NOSQL set data finished"

@app.route("/setup-table")
def sqlconnect():

    print("About to conn")
    #Add your own Postgres Server IP address, PORT, UID, PWD and Database
    conn = psycopg2.connect(
      host=os.environ['DB_HOST'],
      database=os.environ['DB_USERNAME'],
      user='dbappadmin',
      password=os.environ['DB_PASSWORD'])

    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE products (
                product_id int primary key,
                product_name varchar(50),
                price int
                );
                ''')
    conn.commit()

    cursor.execute('''
            INSERT INTO  products(product_id, product_name, price)
            VALUES
                (1,'Desktop Computer',800),
                (2,'Laptop',1200),
                (3,'Tablet',200),
                (4,'Monitor',350),
                (5,'Printer',150);                ''')
    conn.commit()

    #This is just an example

    print('Should have inserted the rows above')
    cursor.close()
    conn.close()
    return "SQL setup/migration finished"

@app.route("/nosql")
def test_nosql():
    users_ref = db.collection(u'users')
    docs = users_ref.stream()
    s = "<table style='border:1px solid red'>"
    for doc in docs:
        docDict = doc.to_dict()
        print(f'{doc.id} => {docDict}')
        s = s + "<tr>"
        s = s + "<td>" + doc.id + "</td>"     
        for x in docDict:    
            s = s + "<td>" + str(x) + ": " + str(docDict[x]) + "</td>"    
        s = s + "</tr>"
    return "<html><body>" + s + "</body></html>"

@app.route("/sql")
def test_sql():
    # creating connection Object which will contain Postgres Connection
    conn = psycopg2.connect(
      host=os.environ['DB_HOST'],
      database=os.environ['DB_USERNAME'],
      user='dbappadmin',
      password=os.environ['DB_PASSWORD'])
    cursor = conn.cursor()    
    cursor.execute("SELECT * FROM products;")    
    s = "<table style='border:1px solid red'>"    
    for row in cursor.fetchall():    
        s = s + "<tr>"    
        for x in row:    
            s = s + "<td>" + str(x) + "</td>"    
        s = s + "</tr>"    
    conn.close()    
    return "<html><body>" + s + "</body></html>"  

# dockerized gunicorn with parametric port 
# if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
