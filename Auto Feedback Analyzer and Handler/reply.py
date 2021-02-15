from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64
from googleapiclient.errors import HttpError
import csv
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://mail.google.com/']

def create_message(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def send_message(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print ('Message Id: %s' % message['id'])
    return message
  except HttpError as error:
    print ('An error occurred: %s' % error)

def start():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    print(service)
    # Call the Gmail API
    results = service.users().messages().list(userId='me').execute()
    #labels = results.get('labels', [])
    with open('file1.csv', 'r', encoding= 'utf-8') as file:
        reader = csv.reader(file)
        for each in reader:
            print(each)
            if each:
                print(each)
                message = create_message('hritik.bnp@gmail.com', each[0], 'TEST', 'Testing')
                send_message(service, 'me', message)
'''
    for message in results.get('messages'):
        print('Message: ' + service.users().messages().get(userId = 'me' , id = message['id']).execute().get('snippet'))
        print('Date: ' + str(service.users().messages().get(userId = 'me' , id = message['id']).execute().get('payload').get('headers')[16]))
        print('Sender: ' + str(service.users().messages().get(userId = 'me' , id = message['id']).execute().get('payload').get('headers')[17]))
        print('Subject: ' + str(service.users().messages().get(userId = 'me' , id = message['id']).execute().get('payload').get('headers')[20]))
        print('\n\n')
'''
'''
    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(type(label['name']))
'''
'''
    with open('file1.csv', 'r', encoding= 'utf-8') as file:
      reader = csv.reader(file)
      for each in reader:
        if each:
          message = create_message('hritik.bnp@gmail.com', each[0], 'TEST'+str(i), 'Testing')
          send_message(service, 'me', message)
'''
'''
    for i in range(20):
        message = create_message('hritik.bnp@gmail.com', 'xhritik.bnp@gmail.com', 'TEST'+str(i), 'Testing')
        send_message(service, 'me', message)

'''
