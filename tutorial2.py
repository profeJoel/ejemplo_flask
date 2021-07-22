from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    #return render_template("theme.html", content=name, other=2)
    #return render_template("theme.html")
    return render_template("theme.html", content = ["Leonardo", "Rafael", "Donatello", "Mike"])

if __name__ == "__main__":
    app.run()