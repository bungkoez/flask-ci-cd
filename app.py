from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    posts = [
        {"title": "Selamat Datang", "content": "Ini adalah blog milik Steephan Riscy Pardingotan Turnip."},
        {"title": "Postingan Pertama", "content": "Halo! Ini adalah postingan pertama saya di blog ini."},
        {"title": "Apa itu Flask?", "content": "Flask adalah framework web Python yang ringan dan mudah digunakan."}
    ]
    return render_template("index.html", posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
