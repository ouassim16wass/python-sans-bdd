from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>bienvenue sur exercice 6'


if __name__ == "__main__":
    app.run(debug=True,port=8080)
