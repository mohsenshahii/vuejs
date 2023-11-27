import pymysql


# Replace with database credentials
host = "localhost"
user = "root"
password = "M0hsensh@hi1"

# Create a connection
conn = pymysql.connect(
    host = host,
    user = user,
    password = password,
)

cursor = conn.cursor()

query = "show databases;"
cursor.execute(query)

result = cursor.fetchall()

for row in result:
    # Access data by column index
    print(row[0])
    

database = input ("choose data base: ")
conn = pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = database
)

cursor = conn.cursor()
# Example query
query = "show tables;"
cursor.execute(query)

result = cursor.fetchall()


for row in result:
    # Access data by column index
    print(row[0])
    


table = input ("choose table: ")
query = f"SELECT * FROM {table}"

cursor.execute(query)

# Fetch the data
result = cursor.fetchall()


for row in result:
    # Access data by column index
    print(row)



values = input ("insert values: ")
query = f"insert into {table} values ({values})"

cursor.execute(query)

# Fetch the data


conn.commit()

cursor.close()
conn.close()
