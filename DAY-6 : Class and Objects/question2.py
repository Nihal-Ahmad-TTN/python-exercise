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

        #initialising the dictionary        
        dictionary={
            "subject": "",
            "date": "",
            "from": "",
            "words": 0,
            "lines": 0,
            "num_attachments": 0,
            "attachments": []
            }
        #dictionary to save the filtered emails in their respective categories
        filter={
            'job': [],
            'image' : [],
            'attachments' : []
        }

        try:
            # Call the Gmail API
            service = build("gmail", "v1", credentials=creds)
            results = service.users().messages().list(userId="me").execute()

            
            #setting limit to fetch only latest 10 emails
            for emails in range(10):

                #getting info about the email using the id
                text = service.users().messages().get(userId="me", id=results['messages'][emails]["id"]).execute()

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


                for item in header:

                    #logic to get date of email
                    if item['name']=="Date":
                        dictionary['date']+=item['value']

                    #logic to get subject of email
                    elif item['name']=='Subject':
                        dictionary['subject']+=item['value']
                    
                    #logic to get senders name and email 
                    elif item['name']=='From':
                        dictionary['from']+=item['value']
                
                #logic to get the attachments name
                for item in part:

                    #checking if the partId starts with 0?
                    if item['partId'].startswith("0"):
                        pass
                    else:

                        #checking if there are attatchments or not
                        if item['filename']=='':
                            continue
                        else:
                            dictionary['attachments'].append(item['filename'])
                
                #logic to get number of attatchments
                dictionary["num_attachments"]+=len(dictionary["attachments"])

                #logic to filter the emails in their respective categories

                #for job
                if '@tothenew.com' in dictionary["from"]:
                    filter['job'].append(dictionary)
                
                #for image and attachments
                else:
                    for item in part:
                        if item['partId'].startswith("0"):
                            pass
                        else:
                            if item['filename']=='':
                                continue
                            else:
                                #checking if its an image
                                if item["mimeType"].startswith("image"):
                                    filter['image'].append(dictionary)
                                else:
                                    filter['attachments'].append(dictionary)

                #resetting the values in dictionary after appending it to filter to check other emails
                dictionary={
                "subject": "",
                "date": "",
                "from": "",
                "words": 0,
                "lines": 0,
                "num_attachments": 0,
                "attachments": []
                }

            #returning the filter
            return filter
            


        except HttpError as error:
            print(f"An error occurred: {error}")
    
    #function to print the respective emails
    def printfile(self, key, res):

        #checking if user asked for job related emails
        if key=="job":
            json_file=json.dumps(res['job'], indent=4)
            print('job emails descriptions : \n',json_file)

        #checking if user asked for image related emails
        elif key=='image':
            json_file=json.dumps(res['image'], indent=4)
            print('image emails descriptions : \n',json_file)

        #checking if user asked for attachment related emails
        elif key=='attachment':
            json_file=json.dumps(res['attachments'], indent=4)
            print('attatchment emails descriptions : \n',json_file)




email_obj=emailread()
valid=['job', 'image', 'attachment']
key=input(" Job / image / attachments : ")
if key.lower() in valid:

    res=email_obj.reademail()
    email_obj.printfile(key, res)
else:
    print("Not a valid term")
    