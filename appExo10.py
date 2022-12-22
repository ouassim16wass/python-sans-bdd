from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form2.html')

@app.route('/resultat2.html', methods=['POST'])
def resultat():
    val1 = request.form["A"]
    val2 = request.form["B"]
    val3 = request.form["C"]
    val4 = request.form["D"]
    resultat = ((int(val1)+int(val2))*int(val3))/int(val4)
    return render_template('resultat2.html', A = val1 , B = val2 , C = val3 , D = val4   , resultat=resultat)



if __name__ == "__main__":
    app.run(debug=True)
