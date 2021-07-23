from flask import Flask, redirect, url_for, render_template, request, session
#perminante session
from datetime import time, timedelta

app = Flask(__name__)
app.secret_key = "hola" #podría ser una mejor password
app.permanent_session_lifetime = timedelta(days=5) #tiempo de session abierta

@app.route("/")
def home():
    return render_template("get_post.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST" :
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/usr")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True) # para editar con el servidor en ejecución