#!/usr/bin/env python
import json
import xmltodict
import json
import requests
from flask import Flask, request, jsonify, abort
app  = Flask(__name__)

@app.route('/findroute', methods=['POST'])
def get_timeschedule():
    params = request.get_json()
    source = params['source']
    dest = params['dest']
    print "source and destination is " , source,dest
    result = []
    newdata = {}
    key="MW9S-E7SL-26DU-VV8V"
    apiurl = "http://api.bart.gov/api/etd.aspx?cmd=etd&orig="+source+"&key="+key
    print "heelo",apiurl
    xmldata = requests.get(apiurl)
    if xmldata.status_code == 200:
       data  = xmldata.content
       mydict = xmltodict.parse(data)
       print json.dumps(mydict,indent=4)
    else:
        raise Exception("Sorry Bart API is not reachable")

    stationinfo = mydict['root']['station']
    destinationinfo = mydict['root']['station']['etd']
    for alldestinations in destinationinfo:
        query = False
	for key,value in alldestinations.items():
            if value == dest:
                print "Found it"
                print key,value
                query = True
            if key == "estimate" and query:
	       for data in value:
                   time = data['minutes']
                   result.append(time)
                   print data['minutes']
               newdata['time'] = result
    return  json.dumps(newdata)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=8090)
