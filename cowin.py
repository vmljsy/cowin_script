from typing import Text
import requests
from datetime import datetime,timedelta
import json

stateid =17
date=(datetime.now()+ timedelta(days=1)).strftime("%d-%m-%Y")
print(date)

nearpincodes=[680681,680682,680683,680684,680685,680686,680687,680688,680689]

#def getdata():
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response= requests.get(f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{stateid}",headers=headers)
print(response.text)
district_id=input('enter the district id  :  ')
response= requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district_id}&date={date}",headers=headers)

response_json=response.json()
for center in response_json["sessions"]:
    print(center["center_id"],center["name"],center["available_capacity_dose1"])
    if center("available_capacity_dose1") >0:
        
#listofcenters=open("cowinData.json","w")
#listofcenters.write(response.text)
#listofcenters.close()

#for i in nearpincodes:
    #response= requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={i}&date={date}",headers=headers)
    #print(response.text)

