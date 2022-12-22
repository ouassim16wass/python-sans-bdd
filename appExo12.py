from flask import Flask, render_template, request

app = Flask(__name__)
persons = [

    {
        "nom":"JOHN","prenom":"DOE","points":15
    },
      {
        "nom":"BOB","prenom":"CARLTON","points":9
    },
      {
        "nom":"RAYANE","prenom":"SMITH","points":13
    }
]





@app.route('/')
def doPersons():
    return render_template("personsData.html" , data=persons)





if __name__ == "__main__":
    app.run(debug=True)
