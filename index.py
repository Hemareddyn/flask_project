# from flask import Flask,render_template
from flask import *
from flask_pymongo import PyMongo

app=Flask(__name__)

mongodb_client=PyMongo(app,uri="mongodb+srv://athumma:Akhila%40123@cluster0.iiybw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db


#calling function from fla
@app.route("/signup",methods=["GET","POST"])
def signup():
    # return "world"
    if request.method== "POST":
        db.user.insert_one(dict(request.form))
        return redirect(url_for('success'))
    return render_template("signup.html")

@app.route('/success')
def success():
    return "success"

@app.route("/login")
def login():
    #return "world"
    return render_template("login.html")    


if __name__ == '__main__':
    app.run()