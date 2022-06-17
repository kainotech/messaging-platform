from twilio.rest import TwilioClient 
 
account_sid = 'AC5156e174961a9c733977d0cfd5e04c58' 
auth_token = "de5d04719f0a8dc1a0484c9eafceb5aa" 
client = TwilioClient(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your Twilio code is 1238432',      
                              to='whatsapp:+94701613315' 
                          ) 
 
print(message.sid)

