import pyodbc
print("About to run C/I build trigger")
#Add your own SQL Server IP address, PORT, UID, PWD and Database
conn = pyodbc.connect(
    'DRIVER={FreeTDS};SERVER=10.29.112.3 ;DATABASE=fisrtdb;UID=firstuser;PWD=Giulio2022', autocommit=True)
cur = conn.cursor()

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
cur.close()
conn.close()
