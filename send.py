import os
from dotenv.main import load_dotenv
import gspread
from mailjet_rest import Client

load_dotenv('.config/.env')

SPREADSHEET_ID = os.environ.get('SPREADSHEET_ID')
MJ_API_KEY     = os.environ.get('MJ_APIKEY_PUBLIC')
MJ_API_SECRET  = os.environ.get('MJ_APIKEY_SECRET')

# # Get the spreadsheet
gc = gspread.service_account(filename='.config/service_account.json')
sh = gc.open_by_key(SPREADSHEET_ID)

settings          = sh.worksheet('Settings')
ios_worksheet     = sh.worksheet('iOS')
android_worksheet = sh.worksheet('Android')

raw_cell = settings.get('A2')
email_message = ''

for r in raw_cell:
    for d in r:
        email_message = d

def sendEmail(worksheet):
    for row in worksheet.get_values()[1:]:
        email = row[0]
        name  = row[1]
        link  = row[2]

        # Send the email
        print('Sending email to {}'.format(email))
        print(email_message.format(name=name, link=link))
        print('=======================================')


print('Bani iOS')
sendEmail(ios_worksheet)

print('Bani Android')
sendEmail(android_worksheet)


# mailjet = Client(auth=(API_KEY, API_SECRET))



