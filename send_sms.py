import africastalking 
import requests

username = "Grey Fish"
api_key = "3390746e38a5e21b5b72349b31daf6b017f13f405c503e54a417fa3cd2b4f11a"
africastalking.initialize(username, api_key)

# Get the SMS service
sms = africastalking.SMS

# Use the service synchronously
response = sms.send("Hello Message!", ["+254724021814"])
print(response)

# Or use it asynchronously
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

sms.send("Hello Message!", ["+2547xxxxxx"], callback=on_finish)