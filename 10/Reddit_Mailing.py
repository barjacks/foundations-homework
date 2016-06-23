
# coding: utf-8

# # Homework_10_Setting_up_Mailgun

import requests


key = 'key-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
sandbox = 'sandboxXXXXXXXXXXXXXXXXXXX.mailgun.org'
recipient = 'barnaby.skinner@sonntagszeitung.ch'

import time
datestring = time.strftime("%m-%h-%d")

request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url,
    auth=('api', key),
    files=[("attachment", open("reddit-frontpage-" + datestring + ".csv"))],
    data={
        'from': 'barnaby.skinner@sonntagszeitung.ch',
        'to': recipient,
        'subject': 'Reddit Frontpage, ' + datestring,
        'text': 'Overview of Reddit Frontpage Stories'
})

print('Status: {0}'.format(request.status_code))
print('Body:   {0}'.format(request.text))


#Checking to see if message is sent
key = 'key-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
sandbox = 'sandbox6XXXXXXXXXXXXXXXXXXXXXXXX.mailgun.org'

request_url = 'https://api.mailgun.net/v2/{0}/events'.format(sandbox)
request = requests.get(request_url, auth=('api', key), params={'limit': 5})

print('Status: {0}'.format(request.status_code))
print('Body:   {0}'.format(request.text))
