import psycopg2

conn = psycopg2.connect(dbname="guacamole_db",
                        user="guacamole_user",
                        host="localhost",
                        password="ChooseYourOwnPasswordHere1234",
                        port="5432")
cur = conn.cursor()


# cur.execute("SELECT * FROM guacamole_user")


cur.execute(open("create-admin-user.sql", "r").read())

rows = cur.fetchall()

for row in rows:
    username = row[1] # assuming username is in the second column
    password = row[2] # assuming password is in the third column
    print("Username:", str(row))
    print("Password:", password)

conn.close()
