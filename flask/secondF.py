from flask import Flask , url_for, render_template, request, redirect
import sqlite3 as sql

# connnection = sql.connect("wesiteUsers.db")
# user = connnection.cursor()
# you have already made tabel called user and with userName and password columns
# user.execute("""create table User(
#              userName text,
#              password text
#  )""")

app = Flask (__name__)


@app.route('/', methods = ['POST','GET'])
def home():

    return render_template('login.html')

@app.route('/mistake')
def mistaken():
            
            return  redirect(url_for("home"))
@app.route('/loginInfo/', methods = ['POST', 'GET'])
def  loginInfo():
     
    infoName = request.form['UserId']
    infoPass  = request.form['passId']
    with sql.connect("wesiteUsers.db")  as connection:
        table = connection.cursor()
        table.execute("select * from User where userName = :name and password = :pass ", {'name': infoName, 'pass': infoPass})
        data = table.fetchone()
        if data:
           return render_template('login2.html', info1 = f'hey {data[0]}  welcome back' )
        else:
            return render_template('login2.html', info1 = 'Account Couldn\'t be found')  

@app.route('/signUpInfo/', methods = ['POST','GET'])
def signUpInfo():
       
        userName = request.form['UserId']
        userPassword = request.form['passId']
        with sql.connect("wesiteUsers.db")  as connection:
            table = connection.cursor()
            table.execute("select * from User where userName = :name ", {'name': userName})
            data = table.fetchone()
            if  not data:
                table.execute("insert into User values (:name, :password)", {'name': userName, 'password':userPassword})
                connection.commit()
                return  render_template('login2.html', info1 = 'signed UP successfully' )
            else:
                 return  render_template('login2.html', info1 = 'Account exists Please recheck your Password' )
                    

@app.route("/signUp/", methods = ['POST','GET'])
def signUp():
       return render_template('signUp.html')


if (__name__) == "__main__":
     app.run(debug=True)
            