import csv
from datetime import datetime
import os
from dotenv import load_dotenv
from notion_client import Client

load_dotenv()

client = Client(auth=os.environ["OAUTH_CLIENT_SECRET"])
database_id = os.environ["database_id"]


def csv_read (csv_file) -> list:
    with open (csv_file, "r+") as csv_:
        csv_data = csv.reader (csv_)
        row_data = []
        for row in csv_data:
            row_data.append(row)
    return row_data


def get_date (date_string) -> str:
    format_ = "%m/%d/%Y"
    formatii_ = "%Y-%m-%d"
    date_ = datetime.strptime(date_string, format_)
    date = date_.strftime(formatii_)
    return date

def create_page (db_id, filename, date):
    response = client.pages.create (**{
        "parent": {
        "database_id": db_id
        },
        "properties": {
            "Filename":{
             "type": "title", 
             "title": [{ "type": "text", "text": { "content": filename } }]
            },
            "Date": {
             "type": "date",
             "date": {"start" : date}
            }

        }
    })
    return response

# ==== 

# 1. Get CSV
csv_data = csv_read ("csv_test2.csv")

# 2. Go through each CSV row and add the page to Notion
for x in range (1, len(csv_data)):
    date = get_date(csv_data[x][1])
    create_page (database_id, csv_data[x][0], date)

# 3. Print a message
print ("Added " + str(len(csv_data)-1) + " pages to the database.")
