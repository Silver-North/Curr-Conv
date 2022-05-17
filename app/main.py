from flask import Flask, render_template, request
from app.module_currency import get_currency, exec_converter 


app = Flask(__name__, static_folder="static")


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "GET":
        context ={
            'currency': get_currency()
        }
    elif request.method == 'POST':
        count_curr = float(request.form['current-value'])
        from_curr = request.form['from']
        to_curr = request.form['to']

        context = {
            'currency': get_currency(),
            'from': from_curr,
            'to': to_curr,
            'curr': count_curr,
            'amount': exec_converter(from_curr, to_curr, count_curr)
        }
    return render_template('home.html', context=context)
