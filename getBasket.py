from time import sleep
import requests
from datetime import datetime, timedelta
from envelopes import Envelope
from cartCheckout import checkout
from orderSummary import summary
from confirmOrder import order
from placeOrder import place

url = "https://www.bigbasket.com/co/delivery-preferences-new/"
cookies = {'sessionid': '1ahwfayyfma1g4z1js8bqauao90k2m6i'}
headers = {'X-Requested-With': 'XMLHttpRequest'}
foundSlotForToday = False
cDate = None
ctr = 0
mySlots = []
print("\nRun Time:", str(datetime.today()))
while True:
    checkDate = (datetime.today() + timedelta(days=2)).strftime('%d-%m-%Y')
    if not cDate == checkDate:
        print('Date changed')
        foundSlotForToday = False
        cDate = checkDate
    print("Running for date", cDate)
    while not foundSlotForToday:
        ctr += 1
        print('Run : ' + str(ctr), str(datetime.today()))
        try:
            response = requests.get(url, headers=headers, cookies=cookies).json()
        except:
            response = "Failed to connect to BigBasket."
            sleep(300)
        try:
            shipment_id = response['details']['shipment_groups'][0]['shipments'][0]['shipment_id']
            fulfillment_id = response['details']['shipment_groups'][0]['shipments'][0]['fulfillment_id']
            linked_shipments = response['details']['shipment_groups'][0]['shipments'][0]['linked_shipments']
            for i in response['details']['shipment_groups'][0]['shipments'][0]['slots']:
                if i['sd_str'] == checkDate:
                    for j in i['slots']:
                        for k in j:
                            if k['available']:
                                foundSlotForToday = True
                                mySlots.append(k)
            if foundSlotForToday:
                error = ''
                printSlots = ''
                for s in mySlots:
                    printSlots += str(s['slot']) + " is available for " + checkDate + "!\n"
                print(printSlots)
                try:
                    summary = summary()
                    val = summary['details']['order_summary']['sub_total']
                    print("Order value :", val)
                    slot = mySlots[0]
                    if float(val) > 600:
                        data = {
                            "book_slots": [
                                {
                                    "slot_date": slot['slot_date'],
                                    "slot_id": slot['slot_id'],
                                    "bb_star_avail": slot['bb_star_avail'],
                                    "shipment_id": shipment_id,
                                    "fulfillment_id": fulfillment_id,
                                    "linked_shipments": linked_shipments
                                }
                            ],
                            "contactless": "false"
                        }
                        out = checkout()
                        print("Checkout :", out)
                        try:
                            order = order(data)
                            print("Order :", order)
                            try:
                                print("Place :", place().json())
                            except:
                                error = "Faliure in place"
                            print(order.json())
                        except:
                            error = "Faliure in order"
                    else:
                        error = "Order value less than 600! Add more items!!\n\n"
                        raise Exception
                except:
                    envelope = Envelope(
                        from_addr=(u'rishabh@bigbasket.com', u'Rishabh Jain'),
                        to_addr=(u'ayushi201098@gmail.com', u'Ayushi Sharma'),
                        cc_addr=(u'yorishabhjain@gmail.com', u'Rishabh Jain'),
                        subject=u'BB Update: Slot is available!',
                        text_body=error + printSlots
                    )
                    print("Error:", error)
                    envelope.send('smtp.googlemail.com', login='yorishabhjain@gmail.com',
                                  password='nvyodlgxuwxviiwv', tls=True)
            else:
                print("No slots found yet for today!")
        except:
            print('Error:', response)
            if "Checkout" in response:
                print("Checkout :", checkout())
        sleep(300)
    sleep(300)
