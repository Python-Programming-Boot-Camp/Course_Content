# pip install gspread oauth2client
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Test").sheet1
data = sheet.get_all_records()

row = sheet.row_values(1)
col = sheet.col_values(3)
cell = sheet.cell(1,2).value
numRows = sheet.row_count
print(numRows)
sheet.append_row([3,2,1])
sheet.update_cell(2,2, "Updated Value")