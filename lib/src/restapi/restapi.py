# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 23:31:27 2021

@author: shubhamchugh
"""
# =============================================================================
# import sys
# sys.path.insert(1,'C:/Users/shubhamchugh/Documents/GitHub/myflaskproject/lib/')
# print(sys.path)
# =============================================================================

from flask import Flask,jsonify,request
from lib.db import dbinterface
from flask_cors import CORS

app=Flask(__name__)

CORS(app)

@app.route("/")
def hello_app():
    try:
        return "Welcome to Flask app"
    except Exception as err:
        print(err)

@app.route("/myflask/v1/category", methods=['GET'])
def category():
    try:
        output=dbinterface.category_data()
        return jsonify(output)
    except Exception as err:
        print(err)
        
@app.route("/myflask/v1/category", methods=['POST'])
def category_input():
    try:
        json_input = request.get_json()
        output=dbinterface.category_data1(json_input)
        return jsonify(output)
    except Exception as err:
        print(err)

@app.route("/myflask/v1/category/<subcategory>", methods=['GET'])
def subcategory_data(subcategory):
    try:
        output=dbinterface.subcategory_data(subcategory)
        return jsonify(output)
    except Exception as err:
        print(err)
        
@app.route("/myflask/v1/<item>", methods=['GET'])
def item_search(item):
    try:
        output=dbinterface.list_of_items(item)
        return jsonify(output)
    except Exception as err:
        print(err)
    
    
if __name__=="__main__":
    try:
        app.run(host="0.0.0.0",port=8081,threaded=True)
    except Exception as err:
        print(err)
  