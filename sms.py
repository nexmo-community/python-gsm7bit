#! /usr/bin/env python3

import gsm7bit
import nexmo

NEXMO_APIKEY = "xxx"
NEXMO_SECRET = "xxx"
destination = 'xxx'

c = gsm7bit.Converter()
client = nexmo.Client(key=NEXMO_APIKEY, secret=NEXMO_SECRET)

while True:
	msg = input("Message:")
	data = c.encode(msg)
	client.send_message({'from':  'Test', 'to': destination, 'type': 'binary',  'udh': '050003CC0101', 'body' : data, 'protocol-id' : '65'})
	