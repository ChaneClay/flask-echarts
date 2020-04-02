from flask import Flask
from flask import render_template

import utils

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/data')
def get_data():
    res = utils.get_data()
    return utils.sort_data(res)


@app.route('/l_data')
def l_data():
    res = utils.get_l_data()
    return utils.age_data(res)


@app.route('/r_data')
def r_data():
    res = utils.get_r_data()
    return utils.income_data(res)


if __name__ == '__main__':
    app.run()
