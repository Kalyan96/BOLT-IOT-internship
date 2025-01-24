import requests # This library is used to make HTTP requests to the Bolt Cloud and Mailgun servers. 
import json # This library is used to convert JSON response received into python style data. 
import time # This library is used to obtain the time data of the VPS. 

key='key-cd7a3123a5403cc1a41da7af677326d4' # e.g. key='key-abcd12n3432lfhafas34asklfj' 
sandbox='https://app.mailgun.com/app/domains/sandboxf7bd4003d85c4c10ae3c2811b52a7231.mailgun.org' 
recipient='kalyanpatnaik96@gmail.com' #you can only send mails to yourself 

def send_mail(body):  # this the function which will append alll the parameters for the meail and send it ot the destination we specify
    request_url='https://api.mailgun.net/v2/{0}/messages'.format(sandbox) 
    request=requests.post(request_url,auth=('api',key),data={ 
    'from':'hello@example.com', 
    'to':recipient, 
    'subject':'Obstacle detected', 
    'text': body 
    }) 
    print ('Status: {0}'.format(request.status_code) )
    print ('Body: {0}'.format(request.text) )

while True: 
    cloud_url = 'http://cloud.boltiot.com/remote/7ff80ce8-b5f0-408f-9e5c-13c40450e46b/analogRead?pin=A0&deviceName=BOLT16256417' 
    r = requests.get(cloud_url) 
    #Proximity sensor output must be given to pin Number 4 of Bolt 
    data = json.loads(r.text) 
    print( data['value']) 
    try: 
        door_opened = int(data['value']) 
        if door_opened < 100 : 
            send_mail("Someone opened your door at " + str(time.time())) 
    except Exception as e: 
        print ("Error",e) 
    time.sleep(5)