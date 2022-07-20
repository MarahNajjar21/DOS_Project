from flask import Flask, request, jsonify
import json
import requests
app = Flask(_name_)
@app.route("/")
def home():
    return "hello world"
@app.route("/info/<id>",methods=['GET'])
def info(id):
    idInt=int(id)
    result=requests.get("http://192.168.1.250:7002/info/{}".format(idInt))
    return (result.content)
@app.route("/search/<topic>",methods=['GET'])
def search(topic):
    result=requests.get("http://192.168.1.250:7002/search/{}".format(topic))
    return (result.content)


@app.route("/IncreaseNumbers",methods=['PUT'])
def IncreaseNumbers():
     id=request.json['ID']
     idInt=int(id)
     amount=request.json['AMOUNTS']
     amountInt=int(amount)
     result=requests.put("http://192.168.1.250:7002/IncreaseNumbers",data={'ID':idInt,'AMOUNTS':amountInt})
     return (result.content)

@app.route("/purchase/<id>",methods=['GET'])
def purchase():
     id=request.json['ID']
     idInt=int(id)
     result=requests.get("http://192.168.1.240:7001/purchase/{}".format(idInt))
     return (result.content)

@app.route("/queryNumbers",methods=['PUT'])

def queryNumbers():
     id=request.json['ID']
     idInt=int(id)
     amount=request.json['AMOUNTS']
     amountInt=int(amount)
     result=requests.put("http://192.168.1.240:7001/queryNumbers",data={'ID':idInt,'AMOUNTS':amountInt})
     return (result.content)


if _name_ == 'main':
    app.run(debug=True, host='0.0.0.0', port=5000)
