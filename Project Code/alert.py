from twilio.rest import TwilioRestClient as Call

From_Number = "+17622165440"
To_Number = "+919962602772"
Src_Path = "https://tarp1.000webhostapp.com/voice.xml"

def call():
    client = Call("AC8c95dafec60efa2f48f101edc18fcd8b","290872cc5b75629a1700c53bb646154c")
    print('Call initiated')
    client.calls.create(to=To_Number, from_=From_Number, url=Src_Path, method = 'Get')
    print('Call has been triggered successfully')
