#################################################### Standard Imports ###########################################################
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#################################################### Module Imports ###########################################################
from ..data_fields import CREDENTIALS_PATH 


#################################################################################################################################
#################################################### Sheet Communication Functions ##############################################
#################################################################################################################################
# This is the sheet id for the location where all the media are to be stored.
# link: https://docs.google.com/spreadsheets/d/12CpXUYHlsGttUsxaArsBuJx0K_oXVFNgvtWUv_g48Nk
ARCHIVE_SHEET_ID = "12CpXUYHlsGttUsxaArsBuJx0K_oXVFNgvtWUv_g48Nk"
ARCHIVE_INATOR_STORAGE_SHEET = "archive_inator_storage"


# This is the needed scopes to access the you google sheets accounts.
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# This function connects to the spreadsheet with the given ARCHIVE_SHEET_ID and credentials. it then returns the spreadsheet object. 
def connect_to_sheet(spreadsheet_id:str = ARCHIVE_SHEET_ID) -> gspread.Spreadsheet:
    print("sheets - [CONNECTING]")
    # Defining credentials and authorizes access.
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_PATH, scope)
    client = gspread.authorize(creds)

        # Opens the spreadsheet with the client and the spreadsheet_id.
        # The "sheet" object is the access point for all reading and writing into the spreadsheet.
    sheet = client.open_by_key(spreadsheet_id)
    print("sheets - [CONNECTION ESTABLISHED]")
    return sheet

# This function reads the number of rows in the given sheet_obj and selected worksheet and writes the given data(with some other sheet specific at the end) in the next empty row.
def write_to_sheet(sheet_obj:gspread.Spreadsheet, data:list[any], worksheet_name:str = ARCHIVE_INATOR_STORAGE_SHEET) -> int:
    """Returns the current amount of media entries in the archive inator storage."""
    archive_sheet = sheet_obj.worksheet(worksheet_name)
    
        # Reads the amount of rows and makes the correct index.
    row_count = len(archive_sheet.col_values(1))
    row_number = row_count+1
    data_insertion_row = "A" + str(row_number)

        # The sheet filter function that will be put at the end of the data list so it appears in the sheets AND all in the "Filtered Data" section.
    archive_sheet_filter_function_tail = ["","",
                                          f"=IF($I$1=\"\";\"\";IF(REGEXMATCH($C{row_number};$I$1);\"CONTAINS\";\"\"))",
                                          f"=IF($J$1=\"\";\"\";IF(AND(REGEXMATCH($C{row_number};$J$1);I{row_number}=\"CONTAINS\");\"CONTAINS\";\"\"))",
                                          f"=IF($K$1=\"\";\"\";IF(AND(REGEXMATCH($C{row_number};$K$1);J{row_number}=\"CONTAINS\");\"CONTAINS\";\"\"))",
                                          f"=IF($L$1=\"\";\"\";IF(AND(REGEXMATCH($C{row_number};$L$1);K{row_number}=\"CONTAINS\");\"CONTAINS\";\"\"))",
                                          "",
                                          f"=IF($I$1=\"\";;IF($J$1=\"\";IF($I{row_number}=\"\";;\"X\");IF($K$1=\"\";IF($J{row_number}=\"\";;\"X\");IF($L$1=\"\";IF($K{row_number}=\"\";;\"X\");IF($L{row_number}=\"\";;\"X\")))))",
                                          f"=IF($N{row_number}=\"X\";A{row_number};\"\")",
                                          f"=IF($N{row_number}=\"X\";B{row_number};\"\")",
                                          f"=IF($N{row_number}=\"X\";C{row_number};\"\")",
                                          f"=IF($N{row_number}=\"X\";D{row_number};\"\")",
                                          f"=IF($N{row_number}=\"X\";E{row_number};\"\")",
                                          f"=IF($N{row_number}=\"X\";F{row_number};\"\")",
                                         ]
        # This appends the filter fuction tail to the data list.
    for i in archive_sheet_filter_function_tail:
        data.append(i)

    print("sheets - [SENDING DATA]")
        # Updates the next row with the given data.
    archive_sheet.update([data], data_insertion_row, raw=False)
    print("sheets - [DATA SENT]")
        # Returns the current amount of media entries in the archive inator storage.
    return row_count