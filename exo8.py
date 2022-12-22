from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
  return render_template ('index.html')

@app.route('/experience')
def index2():
  return render_template ('exper.html')

@app.route('/centre')
def index3():
  return render_template ('centre.html')





if __name__ == "__main__":
    app.run(debug=True,port=5000)
