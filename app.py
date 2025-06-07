from flask import Flask

app = Flask(__name__)

@app.route("/ola")
def ola_mundo():
    return "olá mundo"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
