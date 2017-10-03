import requests
import json

def getList(url):
    url = url+'/projects'
    res = requests.get(url)
    if res.status_code == 200:
        return json.loads(res.content)


def parseProj(url,projId):
    data = getList(url)
    try:
        if data and projId in data['projects'].keys():
            return data['projects'][projId]
        else:
            return None
    except KeyError:
        raise "Error in finding project"
            

def startProj(url,projId):
    if parseProj(url,projId):
        headers = {'Content-type':'application/json'}
        res = requests.post(url+"/start",headers=headers,json={"id":projId})
        #print res.json()

def stopProj(url,projId):
    if parseProj(url,projId):
        headers = {'Content-type':'application/json'}
        res = requests.post(url+"/stop",headers=headers,json={"id":projId})
        #print res.json()


#start VM APP
flaskProj =startProj("http://52.64.2.128:5000/api/v1",'flask')

#stop VM APP
flaskProj =stopProj("http://52.64.2.128:5000/api/v1",'flask')

    
