#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
import vincent
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


### Vincent Data Routes

WIDTH = 600
HEIGHT = 300

@app.route("/data/bar")
def data_bar():
    return vincent.Bar(data.multi_iter1['y1'], width=WIDTH, height=HEIGHT).to_json()


@app.route("/data/line")
def data_line():
    return vincent.Line(data.list_data, width=WIDTH, height=HEIGHT).to_json()


@app.route("/data/multiline")
def data_multiline():
    return vincent.Line(data.multi_iter1, width=WIDTH, height=HEIGHT, iter_idx=('index')).to_json()


@app.route("/data/stocks")
def stocks():
    line = vincent.Line(data.price[['MSFT', 'AAPL']], width=WIDTH, height=HEIGHT)
    line.axis_titles(x='Date', y='Price')
    line.legend(title='MSFT vs AAPL')
    return line.to_json()


@app.route("/data/scatter")
def scatter():
    scatter = vincent.Scatter(data.multi_iter2, width=WIDTH, height=HEIGHT, iter_idx='index')
    scatter.axis_titles(x='Index', y='Data Value')
    scatter.legend(title='Categories')
    return scatter.to_json()


@app.route("/data/stacked_stocks")
def stacked_stocks():
    stacked = vincent.StackedArea(data.price, width=WIDTH, height=HEIGHT)
    stacked.axis_titles(x='Date', y='Price')
    stacked.legend(title='Tech Stocks')
    stacked.colors(brew='Accent')
    return stacked.to_json()


@app.route("/data/stacked_bar")
def stacked_bar():
    stack = vincent.StackedBar(data.df_farm, width=WIDTH, height=HEIGHT)
    stack.axis_titles(x='Total Produce', y='Farms')
    stack.legend(title='Produce Types')
    stack.scales['x'].padding = 0.2
    stack.colors(brew='Pastel1')
    return stack.to_json()


if __name__ == "__main__":
    app.run(debug=True)
