from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! 🚀'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Railway akan set PORT secara otomatis
    app.run(host='0.0.0.0', port=port)  # Penting: host='0.0.0.0'
