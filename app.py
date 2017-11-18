from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
import pandas as pd

#define 4 variables that represent respectively MongoDB IP address, MongoDB port, MongoDB database anme and MongoDB collection name
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'mydb'
COLLECTION_NAME = 'mapbom'
COLLECTION_NAME2 = 'notransposebom'
COLLECTION_NAME3 = 'flow'
COLLECTION_NAME4 = 'newbom2' #trans_combineEFX2.xlsx


app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/example')
def exmaple():
	return render_template("example.html")

@app.route('/mapdata')
def bom():
	connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
	collection = connection[DBS_NAME][COLLECTION_NAME]
	boms = collection.find()
	json_boms = []
	for bom in boms:
		#print(bom)
		json_boms.append(bom)
	json_boms = json.dumps(json_boms, default=json_util.default)
	connection.close()
	return json_boms

@app.route('/mapdata2')
def getdata():
	connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
	collection = connection[DBS_NAME][COLLECTION_NAME]
	boms = collection.find({"ProcType":"E"})
	boms2 = collection.find({"ProcType":"F"})
	json_boms = []
	for bom in boms:
		#print(bom)
		json_boms.append(bom)


	for bom in boms2:
		#print(bom)
		json_boms.append(bom)

	json_boms = json.dumps(json_boms, default=json_util.default)
	connection.close()
	return json_boms


@app.route('/newdata')
def getNewData():
	connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
	collection = connection[DBS_NAME][COLLECTION_NAME2]
	boms = collection.find()
	json_boms = []
	for bom in boms:
		#print(bom)
		json_boms.append(bom)
	json_boms = json.dumps(json_boms, default=json_util.default)
	connection.close()
	return json_boms

@app.route('/newdata2')
def getNewData2():
	connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
	collection = connection[DBS_NAME][COLLECTION_NAME4]
	boms = collection.find()
	json_boms = []
	for bom in boms:
		#print(bom)
		json_boms.append(bom)
	json_boms = json.dumps(json_boms, default=json_util.default)
	connection.close()
	return json_boms



@app.route('/flow')
def getFlow():
	connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
	collection = connection[DBS_NAME][COLLECTION_NAME3]
	flows = collection.find()
	json_boms = []
	for flow in flows:
		#print(bom)
		json_boms.append(flow)
	json_boms = json.dumps(json_boms, default=json_util.default)
	connection.close()
	return json_boms


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000,debug=True)