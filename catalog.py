from flask import Flask, request, jsonify
import json


app = Flask(_name_)

@app.route("/")
def home():
    return "hello world"

@app.route("/info/<id>",methods=['GET'])
def info(id):
    with open('/home/sahar/Desktop/pyox/part1/BooksDB.json', 'r') as DBfile:
        data = DBfile.read()
        jsonObject = json.loads(data)
        BooksRecords = jsonObject['BOOK']
        idInt = int(id)
        result=[BooksRecordsItem for BooksRecordsItem in BooksRecords if BooksRecordsItem['ID'] == idInt]
        if len(result)==0:
            return  "No such Book Found!!"
        return jsonify([{"NUMBERS":result[0]['NUMBERS'],"Title":result[0]['NAME'],"COST":result[0]['COST']}])

@app.route("/search/<topic>",methods=['GET'])
def search(topic):
    with open('/home/sahar/Desktop/pyox/part1/BooksDB.json', 'r') as DBfile:
        data = DBfile.read()
        jsonObject = json.loads(data)
        BooksRecords = jsonObject['BOOK']
        result=[BooksRecordsItem for BooksRecordsItem in BooksRecords if BooksRecordsItem['TOPIC'] == topic]
        arr=[]
        i=0
        for x in result:
            arr.append({"ID":result[i]["ID"],"NAME":result[i]['NAME']})
            i=i+1
        if len(result)==0:
            return  "No Such Book That Have The Same Topic Found!!"
        return jsonify([arr])

@app.route("/updateCost",methods=['PUT'])
def updateCost():
    bodyData=request.data
    with open('/home/sahar/Desktop/pyox/part1/BooksDB.json', 'r') as DBfile:
        data = DBfile.read()
        jsonObject = json.loads(data)
        BooksRecords = jsonObject['BOOK']
    DBfile.close() 
    idInt = int(bodyData['ID'])
    for items in BooksRecords:
      if items["ID"] == idInt:
        items["COST"]=int(bodyData['COST'])   
        newJson=({"BOOK": BooksRecords})
        with open('/home/sahar/Desktop/pyox/part1/BooksDB.json', 'w') as DBfileWrite:
         json.dump(newJson, DBfileWrite,indent=3)
        return "success"

@app.route("/queryNumbers",methods=['PUT'])
def queryNumbers():
    bodyData=request.data
    with open('/home/sahar/Desktop/pyox/part1/BooksDB.json', 'r') as DBfile:
        data = DBfile.read()
        jsonObject = json.loads(data)
        BooksRecords = jsonObject['BOOK']
    DBfile.close() 
    idInt = int(bodyData['ID'])
    amountInt = int(bodyData['AMOUNTS'])
    for items in BooksRecords:
      if items["ID"] == idInt:
          if items["NUMBERS"]!=0:
            items["NUMBERS"]=items["NUMBERS"]-amountInt
            newJson=({"BOOK": BooksRecords})
            with open('/home/sahar/Desktop/pyox/part1/BooksDB.json', 'w') as DBfileWrite:
             json.dump(newJson, DBfileWrite,indent=3)
            return "success"
          else :return "out of stock"
      else: return "NO such book that have same id"

@app.route("/IncreaseNumbers",methods=['PUT'])
def IncreaseNumbers():
    bodyData=request.data
    with open('/home/sahar/Desktop/pyox/part1/BooksDB.json', 'r') as DBfile:
        data = DBfile.read()
        jsonObject = json.loads(data)
        BooksRecords = jsonObject['BOOK']
    DBfile.close() 
    idInt = int(bodyData['ID'])
    amountInt = int(bodyData['AMOUNTS'])
    for items in BooksRecords:
      if items["ID"] == idInt:
            items["NUMBERS"]=items["NUMBERS"]+amountInt 
            newJson=({"BOOK": BooksRecords})
            with open('/home/sahar/Desktop/pyox/part1/BooksDB.json', 'w') as DBfileWrite:
             json.dump(newJson, DBfileWrite,indent=3)
            return "success"
      else: return "NO such book that have same id"
if _name_ == '_main_':

   app.run(debug=True, host='0.0.0.0', port=7002)