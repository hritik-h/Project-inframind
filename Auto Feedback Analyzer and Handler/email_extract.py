
from __future__ import print_function
from datetime import date, timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64
from googleapiclient.errors import HttpError

import io
import csv
import re
SCOPES = ['https://mail.google.com/']
lis = []
today = date.today()
yesterday = today - timedelta(days = 1)
def create_message(sender, to, subject, message_text):

  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def send_message(service, user_id, message):

  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print ('Message Id: %s' % message['id'])
    return message
  except HttpError as error:
    print ('An error occurred: %s' % error)

def extract():
    file = io.open('file1.csv' , 'w' , encoding="utf-8")
    thewriter = csv.writer(file)

    creds = None
    
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    print(service)
    
    query = "before: {0} after: {1}".format(today.strftime('%Y/%m/%d'),
                                        yesterday.strftime('%Y/%m/%d'))
    results = service.users().messages().list(userId='me', q = query).execute()
    
    for message in results.get('messages'):
        for each in service.users().messages().get(userId = 'me' , id = message['id']).execute().get('payload').get('headers'):
            if each.get('name') == 'From':
              email = each.get('value')
        lis.append([re.findall("([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)" , email)[0] , service.users().messages().get(userId = 'me' , id = message['id']).execute().get('snippet')])
        thewriter.writerow([re.findall("([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)" , email)[0] , service.users().messages().get(userId = 'me' , id = message['id']).execute().get('snippet')])
        
    return lis

