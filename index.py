from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('reg.html')

@app.route("/reg.html")
def inicio():
    return render_template('reg.html')

@app.route("/venda1.html")
def item1():
    return render_template('venda1.html')

@app.route("/venda2.html")
def item2():
    return render_template('venda2.html')

@app.route("/venda3.html")
def item3():
    return render_template('venda3.html')

@app.route("/venda4.html")
def item4():
    return render_template('venda4.html')

@app.route("/venda5.html")
def item5():
    return render_template('venda5.html')

@app.route("/venda6.html")
def item6():
    return render_template('venda6.html')

@app.route("/venda7.html")
def item7():
    return render_template('venda7.html')

@app.route("/venda8.html")
def item8():
    return render_template('venda8.html')

@app.route("/venda9.html")
def item9():
    return render_template('venda9.html')

@app.route("/venda10.html")
def item10():
    return render_template('venda10.html')

@app.route("/venda11.html")
def item11():
    return render_template('venda11.html')

@app.route("/venda12.html")
def item12():
    return render_template('venda12.html')

@app.route("/efetuada.html")
def compra():
    return render_template('efetuada.html')


if __name__ == '__main__':
    app.run(debug=True)