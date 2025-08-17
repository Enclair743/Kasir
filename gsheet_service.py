import gspread
from oauth2client.service_account import ServiceAccountCredentials

GSHEET_ID = "1fMk74h7dTuKz2QjYY9guMPeOeBxQPrWRDtqWfoA87wA"
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

def get_client():
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "service_account.json", SCOPE
    )
    return gspread.authorize(creds)

def get_sheet(sheet_name):
    client = get_client()
    return client.open_by_key(GSHEET_ID).worksheet(sheet_name)

def get_records(sheet_name):
    sheet = get_sheet(sheet_name)
    return sheet.get_all_records()

def append_row(sheet_name, row_data):
    sheet = get_sheet(sheet_name)
    sheet.append_row(row_data)

def update_row(sheet_name, row_num, row_data):
    sheet = get_sheet(sheet_name)
    sheet.update(f'A{row_num}:F{row_num}', [row_data])

def find_row(sheet_name, key, value):
    records = get_records(sheet_name)
    for idx, record in enumerate(records, start=2):  # header di row 1
        if record.get(key) == value:
            return idx, record
    return None, None
