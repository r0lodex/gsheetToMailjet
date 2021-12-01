import os
import gspread
from mailjet_rest import Client


# Get the spreadsheet
gc = gspread.service_account()


# Send the email
API_KEY = os.environ.get('MJ_APIKEY_PUBLIC')
API_SECRET = os.environ.get('MJ_APIKEY_SECRET')

mailjet = Client(auth=(API_KEY, API_SECRET))



