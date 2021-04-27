from twilio.rest import Client

client = Client()

message = client.messages.create(
    to="+5538999285756",
    from_="+38991801928",
    body="Hello from Python!")

print(message.sid)