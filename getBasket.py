from time import sleep
import requests
from datetime import datetime, timedelta
from envelopes import Envelope

url = "https://www.bigbasket.com/co/delivery-preferences-new/"
cookies = {'sessionid': '1ahwfayyfma1g4z1js8bqauao90k2m6i'}
headers = {'X-Requested-With': 'XMLHttpRequest'}
foundSlotForToday = False
cDate = None
ctr = 0
mySlots = []
print(datetime.today())
while True:
    checkDate = (datetime.today() + timedelta(days=2)).strftime('%d-%m-%Y')
    print('Running for date ' + cDate)
    if not cDate == checkDate:
        foundSlotForToday = False
        cDate = checkDate
        print('Date changed')
    while not foundSlotForToday:
        ctr += 1
        print('Run : ' + str(ctr))
        response = requests.request("GET", url, headers=headers, cookies=cookies).json()
        for i in response['details']['shipment_groups'][0]['shipments'][0]['slots']:
            if i['sd_str'] == checkDate:
                for j in i['slots']:
                    for k in j:
                        if k['available']:
                            foundSlotForToday = True
                            mySlots.append(k)
                            printSlots = ''
                            for s in mySlots:
                                printSlots += str(s['slot']) + " is available for " + checkDate + "!\n"
                            envelope = Envelope(
                                from_addr=(u'rishabh@bigbasket.com', u'Rishabh Jain'),
                                to_addr=(u'a~yushi201098@gmail.com', u'Ayushi Sharma'),
                                cc_addr=(u'yorishabhjain@gmail.com', u'Rishabh Jain'),
                                subject=u'BB Update: Slot is available!',
                                text_body=printSlots
                            )
                            print(printSlots)
                            envelope.send('smtp.googlemail.com', login='yorishabhjain@gmail.com',
                                          password='nvyodlgxuwxviiwv', tls=True)
    sleep(300)
