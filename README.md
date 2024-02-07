# notion_csv_addpages

This console app is part of my Tiktok Backup Suite (https://github.com/mnettl/video_backups). It takes the csv file outputted by ``writefilescsv.py`` and adds each row as a page in a Notion database.


## Instructions

1 - You must have a Notion API token to run this app. Instructions for obtaining an API token can be found here (https://developers.notion.com/docs/authorization). 

1a. Add the token to the .env file:

```plaintext
OAUTH_CLIENT_SECRET="the Notion API token"
```

1b. Add the Notion database ID to the .env file. Instructions for obtaining the database ID can be found here (https://developers.notion.com/reference/retrieve-a-database)

```plaintext
database_id ="the Notion database id"
```

2 - ``csv.csv`` must be in the same folder as ``notion_csv_addpages.py``

3 - run ``notion_csv_addpages.py`` in the terminal:

```bash
python3 notion_csv_addpages.py
```
The app will add the rows to the Notion database. 

## Requirements
- Python 3
- Python ``python-dotenv`` package
- Python ``csv`` package
- Unix

