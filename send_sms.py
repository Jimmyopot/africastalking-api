import requests

url = 'https://api.sandbox.africastalking.com/version1/messaging'  # set url  
        
headers = {
    'ApiKey': "94aab9f6f6417aca4ddc6f035861518cd469a9d9cf037d58f055a72bbdf58a89", 
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json'
}

data = {
    'username': "greyfish",
    'from': "59879",
    'message': "Hi there...",
    'to': "+254724021814",
}

def make_post_request():  
    response = requests.post(url=url, headers=headers, data=data )
    return response

print(make_post_request().json())

