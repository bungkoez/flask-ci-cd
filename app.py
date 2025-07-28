from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("style.css")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # WAJIB GUNAKAN PORT DARI ENV
    app.run(host="0.0.0.0", port=port)
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # ini perlu file templates/index.html

@app.route("/about")
def about():
    return render_template("about.html")  # ini juga

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
