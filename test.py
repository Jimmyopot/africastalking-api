# works with both python 2 and 3
from __future__ import print_function

import africastalking

class SMS:
    def __init__(self):
		# Set your app credentials
        self.username = "Grey Fish"
        self.api_key = "94aab9f6f6417aca4ddc6f035861518cd469a9d9cf037d58f055a72bbdf58a89"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
            # Set the numbers you want to send to in international format
            recipients = ["+254724021814"]

            # Set your message
            message = "I'm a lumberjack and it's ok, I sleep all night and I work all day";

            # Set your shortCode or senderId
            sender = "shortCode or senderId"
            try:
				# Thats it, hit send and we'll take care of the rest.
                response = self.sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print ('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
    SMS().send()