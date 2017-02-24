import requests
import json
import xmltodict
import pymongo
def get_stationinfo():

    r = requests.get("http://api.bart.gov/api/stn.aspx?cmd=stns&key=MW9S-E7SL-26DU-VV8V")
    data = r.content
    dict = xmltodict.parse(data)
    stationinfo = {}
    for station in dict['root']['stations']['station']:
        name = station['name']
        abbr =  station['abbr']
        stationinfo[abbr] = name
    return stationinfo
