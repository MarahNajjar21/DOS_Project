from xml.dom.minidom import TypeInfo
from flask import Flask, request, jsonify
import json
import requests

app = Flask(_name_)

@app.route("/")
def home():
    return "hello"

@app.route("/purchase/<id>",methods=['GET'])
def purchase(id):
    idInt = int(id)
    #result=requests.get("http://192.168.1.240:7010/info/{}".format(idInt))
    #if(result.json()["info"][0]["NUMBERS"]>0):
    buyResult=requests.put("http://192.168.137.68:7018/queryNumbers/{}".format(idInt),data=json.dumps({'AMOUNTS':1}))
    type(json.dumps({'AMOUNTS':1}))
    return buyResult.content
    #text,buyResult.status_code,buyResult.headers.items()
    
    #else :return ({"msg":"out of stock!!"})
    
if _name_ == '_main_':

   app.run(debug=True, host='0.0.0.0', port=7001)
