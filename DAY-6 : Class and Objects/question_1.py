import os.path
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

class emailread:

  def reademail(self):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
      creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open("token.json", "w") as token:
        token.write(creds.to_json())

    #initialising the dictionary to store the datas from the emails
    dictionary={
        "subject": "",
        "date": "",
        "from": "",
        "words": 0,
        "lines": 0,
        "num_attachments": 0,
        "attachments": []
      }
    
    #initialising the email_info variable to store infos of various emails
    email_info=[]

    try:
      # Call the Gmail API
      service = build("gmail", "v1", credentials=creds)
      results = service.users().messages().list(userId="me").execute()
      
      #restricting to fetch only latest 10 emails
      for email in range(10):

        #getting info about the email using the id
        text = service.users().messages().get(userId="me", id=results['messages'][email]["id"]).execute()

        #initialising variables
        body=text['snippet']
        header= text['payload']['headers']
        part=text['payload']['parts']

        #logic for calculating lines in body of email
        dictionary['lines']+=len(body.split())

        #logic for calculating no of words in email body
        words=0
        for lines in body.split():
          words+=len(lines)
        dictionary['words']+=words
        
        #logic to get attachment of email
        for item in part:

          #checking if the partId starts with 0
          if item['partId'].startswith("0"):
            pass

          else:
            #checking if the attachment section is empty
            if item['filename']=='':
              pass
            else:
              dictionary['attachments'].append(item['filename'])

        for item in header:
          #logic to get date of email
          if item['name']=="Date":
            dictionary['date']+=item['value']

          #logic to get subject of email
          elif item['name']=='Subject':
            dictionary['subject']+=item['value']

          #logic to get sender name of email
          elif item['name']=='From':
            dictionary['from']+=item['value']

        #logic to get number of attachments of email
        dictionary["num_attachments"]+=len(dictionary["attachments"])

        #appending the info gained into email_info list
        if dictionary['num_attachments']>0:
          email_info.append(dictionary)

        #resetting the value of dictionary for next emails
        dictionary={
        "subject": "",
        "date": "",
        "from": "",
        "words": 0,
        "lines": 0,
        "num_attachments": 0,
        "attachments": []
        }

      #creating email.json file and writing the json in it
      with open('email.json','w') as file:

        json_file=json.dumps(email_info, indent=4)
        file.write(json_file)

    except HttpError as error:
      print(f"An error occurred: {error}")


email_obj=emailread()
email_obj.reademail()