# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 23:31:51 2021

@author: shubhamchugh
"""

import pymongo
from config import config 
import datetime

def connect_db():
    try:
        url=config.DB_URL
        db_name=config.DB_NAME
        client=pymongo.MongoClient(url)
        con=client[db_name]
        return con
    except pymongo.errors.ConnectionFailure as err:
        print(err)
    except Exception as err:
        print(err)
        
def category_data():
    try:
        db=connect_db()
        output=[]
        category_data=db.category_data()
        for s in category_data:
            output.append(s)
        return output
    except Exception as err:
        print(err)
        
def category_data1(json_input):
    try:        
        db=connect_db()
        info =db.category_data
        category=       json_input['category']
        date_created=datetime.datetime.utcnow()
        info.insert_one({'date_created':date_created,'category':category})
        return ({'category':category,'date_created':date_created})
    except Exception as err:
        print(err)

    
    
def subcategory_data(subcategory):
    try:
        db=connect_db()
        output=[]
        subcategory=db.subcategory_data()
        for s in subcategory.find({"subcategory":subcategory}):
            output.append(s)
        return output
    except Exception as err:
        print(err)

def list_of_items(item):
    try:
        db=connect_db()
        output=[]
        listofitems=db.list_of_items()
        for s in listofitems.find({"item":item}):
            output.append(s)
        return output
    except Exception as err:
        print(err)
        
        
        
        