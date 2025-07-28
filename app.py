from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Untuk deployment di Railway, harus pakai host 0.0.0.0 dan port 8000
    app.run(host='0.0.0.0', port=8000)
