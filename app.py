from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá! Essa é a minha primeira página de back-end criada no GitHub!"

if __name__ == "__main__":
    app.run()
