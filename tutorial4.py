from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("get_post.html")

@app.route("/login", methods = ["POST", "GET"])
def home():
    return render_template()

@app.route("/<usr>")
def home(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True) # para editar con el servidor en ejecución