import sqlite3

connnection = sqlite3.connect("wesiteUsers.db")
user = connnection.cursor()

# user.execute("""create table User(
#              userName text,
#              password text
# )""")

user.execute("select * from user")
print(user.fetchall())