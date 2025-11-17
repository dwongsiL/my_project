from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Xin chao, toi dang tap lam DevSecOps"

@app.route('/health')
def  health():
    return "Status: OK", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)