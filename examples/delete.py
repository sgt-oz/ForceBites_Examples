"""delete(): delete the records listed in a DataFrame's Id column.

Removes every Contact with the first name "ForceBites". The other scripts delete their own when they
finish, so this cleans up after one that stopped partway. Attachments go with their Contacts, and
deleted records go to the Recycle Bin.

To run it (steps 1 and 2 are only needed once):
    1. pip install forcebites python-dotenv
    2. Copy .env.example to .env, both in the repo folder, and fill in your connected app's details.
    3. python examples/delete.py
"""

import os
from dotenv import load_dotenv
from forcebites import Salesforce

load_dotenv()
sf = Salesforce(os.environ["SFCONSUMERKEY"], os.environ["SFCONSUMERSECRET"], domain=os.environ["SFDOMAIN"], refresh_token=os.environ.get("SFRFRESHTOKEN") or None)
df = sf.query("SELECT Id FROM Contact WHERE FirstName = 'ForceBites'")
successful, failed = sf.delete(df, "Contact")
print(successful)  # the rows deleted
print(failed)  # the rows that weren't, plus an Error column saying why
