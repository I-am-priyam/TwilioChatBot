from flask import Flask
from flask import request
from twilio.rest import Client
import os
app = Flask(__name__)

ACCOUNT_ID=os.environ.get('TWILIO_ACCOUNT')
TWILIO_TOKEN=os.environ.get('TWILIO_TOKEN')
TWILIO_NUMBER='whatsapp:+14155238886'

client=Client('ACae9387f589f2dc42b08c5770f301586a','4f545a6c92a7629a5599d52a2e095459')

def process_msg(msg):
    response=""
    if msg=='hi':
        response="hello welcome to the stock market's chat bot"
    else:
        response="Please type hi to get started"
    return response

def send_msg(msg,recipient):
    try:
        client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
        )
    except:
        print('error')
'''@app.route('/')
def hello():
    return "Hello World!"
'''

@app.route('/webhook',methods=['POST'])
def webhook():
    #import pdb
    #pdb.set_trace()
    try:
        f=request.form 
        msg=f['Body']
        sender=f['From']
        response=process_msg(msg)
        send_msg(response,sender)
        return "Result ok"
    except:
        print("Result not ok")
'''if __name__ == '__main__':
    app.run()'''