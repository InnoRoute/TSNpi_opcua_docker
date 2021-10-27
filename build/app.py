from flask import Flask, request, jsonify
from opcua import Client
from opcua import ua
import time


app = Flask(__name__)

@app.route('/get',  methods=['POST'])
def get():
	request_data=request.get_json(force=True)
	client=request_data["CLIENT"]
	path=request_data["PATH"]
	print(client)
	print(path)
	try:
		client = Client(client)
		client.connect()
		root = client.get_root_node()
		resp=str(root.get_child(path).get_value())
		client.disconnect()
		return jsonify({'status':'OK','msg':"","response":str(resp)}),200
	except Exception as e:
		return jsonify({'status':'ERROR','msg':str(e)}),401

@app.route('/call',  methods=['POST'])
def call():
	request_data=request.get_json(force=True)
	client=request_data["CLIENT"]
	path=request_data["PATH"]
	method=request_data["METHOD"]
	print(client)
	print(path)
	try:
		client = Client(client)
		client.connect()
		root = client.get_root_node()
		
		resp=str(root.get_child(path).call_method(method,request_data["PARAM1"] ))
		client.disconnect()
		return jsonify({'status':'OK','msg':"","response":str(resp)}),200
	except Exception as e:
		return jsonify({'status':'ERROR','msg':str(e)}),401
	
	
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001)
    
    
    
    
    
