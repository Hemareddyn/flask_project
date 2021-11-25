from flask import Flask,render_template

app=Flask(__name__)


#calling function from fla
@app.route("/signup")
def signup():
    # return "world"
    return render_template("signup.html")

@app.route("/login")
def login():
    # return "world"
    return render_template("login.html")    

if __name__ == '__main__':
    app.run()