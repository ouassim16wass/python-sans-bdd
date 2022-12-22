from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/result', methods=['GET'])
def resultat():
    maval1= request.args.get("A")
    maval2= request.args.get("B")
    maval3= request.args.get("C")
    result = int(maval1)+int(maval2)+int(maval3)
    return render_template('resultat.html', A = maval1 , B = maval2 , C = maval3 , resultat=result)
if __name__ == "__main__":
    app.run(debug=True)