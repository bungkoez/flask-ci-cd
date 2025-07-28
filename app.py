from flask import Flask, render_templates

app = Flask(__name__)

@app.route("/")
def home():
    return render_templates("index.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
