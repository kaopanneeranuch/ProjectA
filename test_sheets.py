import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from json import loads

scope = ['https://spreadsheets.google.com/feeds']
creds_dict = loads(os.getenv('GOOGLE_SHEETS_CREDS'))
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

sheet = client.open_by_key('1ILu-zI_Ws2NEdyZnbqOpcEQDj0v9G24IHYxPQYHyrNo')

list_of_values = [['Test', 'GCP'], ['SIIT', 'ProjectA']]
sheet.sheet1.insert_rows(list_of_values, 1)