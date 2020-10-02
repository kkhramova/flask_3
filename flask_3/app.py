from flask_3.request import Request
from flask import Flask
from datetime import date
from flask import render_template

app = Flask(__name__)


@app.route('/nbu')
def index():
    res = Request()
    response = res.get_resp()
    json_res = res.content_type(response.content)
    if json_res is None:
        return 'parsing error'
    if response is None:
        return 'failed to get response'
    if response.status_code != 200:
        return 'the request was not fulfilled'
    return render_template('index.html')


date = date.today()
