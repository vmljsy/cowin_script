from typing import Text
import requests
from datetime import datetime,timedelta
import json
import config
import schedule
import time  



flag=0
stateid =17
date=(datetime.now()+ timedelta(days=1)).strftime("%d-%m-%Y")
print(date)


def telegram_bot_sendtext(bot_message):
    
    send_text = 'https://api.telegram.org/bot' + config.bot_token + '/sendMessage?chat_id=' + config.bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def convertTuple(tup):
    str =  ''.join(tup)
    return str

def repeat(flag1):
    flag1
    for i in range(20):
        def getdata(flag1):
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            response= requests.get(f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{stateid}",headers=headers)
            print(response.text)
            district_id=303  #input('enter the district id  :  ')
            response= requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district_id}&date={date}",headers=headers)

            response_json=response.json()
            if flag1!=1:
                telegram_bot_sendtext("Bot started")

            for center in response_json["sessions"]:
                if center["available_capacity_dose1"]>0:
                    msg ="Center no: "+str(center["center_id"])+"\nCenter Name: " +str(center["name"])+"doses available: " +str(center["available_capacity_dose1"])
                    print(msg)
                    telegram_bot_sendtext(msg)
                    flag1 =1
        time.sleep(5*60)

if __name__ == '__main__':
    repeat(flag)



#schedule.every(5).minutes.do(getdata(flag))







#listofcenters=open("cowinData.json","w")
#listofcenters.write(response.text)
#listofcenters.close()

#for i in nearpincodes:
    #response= requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={i}&date={date}",headers=headers)
    #print(response.text)

