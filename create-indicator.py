
import asyncio
import json
from requests.auth import HTTPBasicAuth
import requests
from time import sleep

import xlrd

# Addresses
BASE_URL = 'https://dhis2_server/'

# authentication
username = 'username'
password = 'passoerd'

headers = {
'Content-type': 'application/json',
'Authorization': 'Basic {BSCAUTH}'
}

async def create_indicator(indicator):
    url = BASE_URL + "api/indicators"
    return requests.post(url, headers=headers, data=json.dumps(indicator))
     



async def main():
    file_loc = ("./metadata/OrderFulfilment.xlsx")
    wb = xlrd.open_workbook(file_loc)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    for count in range(rows):
        if count > 0:
            print(sheet.cell_value(count, 1))
            indicator = {
                "id": sheet.cell_value(count, 3),
                "name": sheet.cell_value(count, 0),
                "shortName": sheet.cell_value(count, 1)[0:50],
                "denominatorDescription": sheet.cell_value(count, 7),
                "numeratorDescription": sheet.cell_value(count, 5),
                "numerator": sheet.cell_value(count, 4),
                "denominator": sheet.cell_value(count, 6),
                "annualized": False,
                "dimensionItemType": "INDICATOR",
                "indicatorType": {
                    "id": "rkNUnbT3eAE"
                }
            }
            print(json.dumps(indicator))
            response = await create_indicator(indicator)
            print(response)

asyncio.run(main())