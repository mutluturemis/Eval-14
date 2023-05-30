#resconf-put.py
import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://10.176.160.12/restconf/data/ietf-interfaces:interfaces/interface=Loopback"

headers = { "Accept": "application/yang-data+json",
"Content-type":"application/yang-data+json"
}

basicauth = ("cisco", "cisco123!")

yangConfig = {
"ietf-interfaces:interface": {
"name": "Loopback",
"description": "My second RESTCONF loopback",
"type": "iana-if-type:softwareLoopback",
"enabled": True,
"ietf-ip:ipv4": {
"address": [
{
"ip": "200.200.200.200",
"netmask": "255.255.255.0"
}
]
},
"ietf-ip:ipv6": {}
}
}

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
print("STATUS OK: {}".format(resp.status_code))
else:
print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))
#end of file