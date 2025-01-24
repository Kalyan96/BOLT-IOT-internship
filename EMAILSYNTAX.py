import requests # This library is used to make HTTP requests to the Bolt Cloud and Mailgun servers. 

key='' # e.g. key='key-abcd12n3432lfhafas34asklfj' 
sandbox='YOUR SANDBOX URL HERE' 
recipient='YOUR EMAIL HERE' # you can only send mails to yourself 

request_url='https://api.mailgun.net/v2/{0}/messages'.format(sandbox) 
request=requests.post(request_url,auth=('api',key),data={ 
    'from':'hello@example.com', 
    'to':recipient, 
    'subject':'Hello', 
    'text':'Hello from Mailgun' 
}) 
print 'Status: {0}'.format(request.status_code) 
print 'Body: {0}'.format(request.text)