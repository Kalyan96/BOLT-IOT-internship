import requests
import time
import json

reada0="http://cloud.boltiot.com/remote/7ff80ce8-b5f0-408f-9e5c-13c40450e46b/analogRead?pin=A0&deviceName=BOLT16256417";
ond0="http://cloud.boltiot.com/remote/7ff80ce8-b5f0-408f-9e5c-13c40450e46b/digitalMultiWrite?pins=0&states=1&deviceName=BOLT16256417";
offd0="http://cloud.boltiot.com/remote/7ff80ce8-b5f0-408f-9e5c-13c40450e46b/digitalMultiWrite?pins=0&states=0&deviceName=BOLT16256417";
while True:
    r=requests.get(reada0);
    a=json.loads(r.text);
    if int(a['value']) < 100 :
        r=requests.get(ond0)
    else :
        r=requests.get(offd0)
    print("distance is: ")
    print(a['value'])
    
    
                            
                            
              