from twilio.rest import TwilioRestClient
 
'''
Twilio is used here to send mobile SMS.
To use this, you first have to create an account on www.twilio.com.
After registering, you will get an ID, a token and a Twilio number.
'''


account_sid = "AC73f141bc5xxxxxxxxxxxxxxxxxx" # Account Sid
auth_token  = "43f1e4b3d18xxxxxxxxxxxxxxxx" # Account Token

client = TwilioRestClient(account_sid, auth_token)
 
def send_sms(text):
    message = client.messages.create(body=text,
    to="+9199xxxxxxxx",    # Alerts will be send to this number
    from_="+1530xxxxxxxx") # Your twilio number
    print message.sid



