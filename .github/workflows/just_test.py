range_ = "A1:C5" # Replace with the range of cells you want to frame
requests = [
    {
        "updateBorders": {
            "range": {
                "sheetId": sheet_id, # Replace with the sheet ID of your sheet
                "startRowIndex": range_.start_row_index,
                "endRowIndex": range_.end_row_index,
                "startColumnIndex": range_.start_col_index,
                "endColumnIndex": range_.end_col_index,
            },
            "bottom": {
                "style": "SOLID",
                "width": 1,
                "color": {
                    "red": 0,
                    "green": 0,
                    "blue": 0,
                },
            },
            "top": {
                "style": "SOLID",
                "width": 1,
                "color": {
                    "red": 0,
                    "green": 0,
                    "blue": 0,
                },
            },
            "left": {
                "style": "SOLID",
                "width": 1,
                "color": {
                    "red": 0,
                    "green": 0,
                    "blue": 0,
                },
            },
            "right": {
                "style": "SOLID",
                "width": 1,
                "color": {
                    "red": 0,
                    "green": 0,
                    "blue": 0,
                },
            },
        }
    }
]
response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body={"requests": requests}).execute()
