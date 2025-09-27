#################################################### Standard Imports ###########################################################
import gspread
from oauth2client.service_account import ServiceAccountCredentials


#################################################################################################################################
#################################################### Sheet Communication Functions ##############################################
#################################################################################################################################
# This is the sheet id for the location where all the movies are to be stored.
# link: https://docs.google.com/spreadsheets/d/12CpXUYHlsGttUsxaArsBuJx0K_oXVFNgvtWUv_g48Nk
ARCHIVE_SHEET_ID = "12CpXUYHlsGttUsxaArsBuJx0K_oXVFNgvtWUv_g48Nk"
CREDENTIALS_PATH = "src_code/credentials.json"
ARCHIVE_INATOR_STORAGE_SHEET = "archive_inator_storage"

# This is the needed scopes to access the you google sheets accounts.
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]

# This function connects to the spreadsheet with the given ARCHIVE_SHEET_ID and credentials. it then returns the spreadsheet object. 
def connect_to_sheet(spreadsheet_id:str = ARCHIVE_SHEET_ID) -> gspread.Spreadsheet:
    # Defining credentials and authorizes access.
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_PATH, scope)
    client = gspread.authorize(creds)

        # Opens the spreadsheet with the client and the spreadsheet_id.
        # The "sheet" object is the access point for all reading and writing into the spreadsheet.
    sheet = client.open_by_key(spreadsheet_id)
    return sheet

# This function reads the number of rows in the given sheet_obj and selected worksheet and writes the given data in the next row.
def write_to_sheet(sheet_obj:gspread.Spreadsheet, data:list[list[any]], worksheet_name:str = ARCHIVE_INATOR_STORAGE_SHEET) -> int:
    """Returns the current amount of media entries in the archive inator storage."""

    archive_sheet = sheet_obj.worksheet(worksheet_name)

        # Reads the amount of rows.
    row_count = len(archive_sheet.col_values(1))
    data_insertion_row = "A" + str(row_count+1)
    print("Data Recived")

        # Updates the next row with the given data.
    archive_sheet.update(data, data_insertion_row)
    print("Data Sent")
        # Returns the current amount of media entries in the archive inator storage.
    return row_count
