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
    result=requests.get("http://192.168.137.68:7018/info/{}".format(idInt))
    return (result.content)
@app.route("/search/<topic>",methods=['GET'])
def search(topic):
    result=requests.get("http://192.168.137.68:7018/search/{}".format(topic))
    return (result.content)

@app.route("/purchase/<int:id>",methods=['GET'])
def purchase(id):
     id=request.json['ID']
     idInt=int(id)
     result=requests.get("http://192.168.137.73:7001/purchase/{}".format(idInt))
     return (result.content)




if _name_ == 'main':
    app.run(debug=True, host='0.0.0.0', port=5000)
