from twilio.rest import Client

account_sid = 'AC302ee1b6bb63c779a40e211655ae233e'
auth_token = '5a2aa76d076c0d47536c1b2e5534b3d1'
client = Client(account_sid, auth_token)

def send():
    message = client.messages.create(
                                  to='+918850145561',
                                  from_='+12052933688',
                                  body="Alert! Your freezer has been opened for over 2 minutes! Ignore if freezer is being filled."
                              )

    print(message.sid)
