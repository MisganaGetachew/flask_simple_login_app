from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
def home ():
        
        return "hello! this my f pro <h1>hello masters!<h1>"


@app.route('/grade/', methods = ['POST', 'GET'])
def grade():
        result = request.form
        value  = 0
        for val, sc in result.items():
                value += int(sc)
                
        return render_template('result.html', people = result, sum = value )
        
        


# @app.route("/<name>")
# def user(name):
#     return f"hello! <h1> {name}<h1>"

# @app.route("/mistake")
# def mistaken():
            
#             return  redirect(url_for("home"))

# @app.route('/score/')
# def scores():
#      peoplesScore = {"Abebe": 55, "Misge": 99, "Zeleke": 34}
#      return render_template('result.html', people = peoplesScore)
# @app.route('/success/<name>')
# def success(name):

#    return render_template('index.html', mk = name )

# @app.route('/blog/<int:postID>')
# def show_blog(postID):
#    return f"when multiplied by two = {postID * 2}"

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))       

if (__name__) == "__main__":
        app.run(debug=True)
