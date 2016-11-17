from twilio.rest import TwilioRestClient
 
client = TwilioRestClient('ACb482914bfed498ebab0bc6a28d5b9baf','875daa56b7b21d4dbfc3055526f7f3c6')
 
client.messages.create(from_='18315401397',
                       to='18316767386',
                       body='Bro you better watch yo back someone just crossed your fn sensor bro....')
print('text sent')
