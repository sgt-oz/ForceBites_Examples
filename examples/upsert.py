"""upsert(): update the record each row matches, or create one when there's no match.

Inserts the 5,000 made-up Contacts in data/contacts.csv, then upserts them along with 100 new rows,
matching on "Id": the inserted rows have an Id, so they update their Contact, and the new rows
don't, so they create one. Every row gets " (upserted)" added to its last name. Then it deletes
them all again.
An External ID field works the same way: pass its name instead of "Id". Use a sandbox.

To run it (steps 1 and 2 are only needed once):
    1. pip install forcebites python-dotenv
    2. Copy .env.example to .env, both in the repo folder, and fill in your connected app's details.
    3. python examples/upsert.py
"""

import os
import pandas as pd
from dotenv import load_dotenv
from forcebites import Salesforce

load_dotenv()
sf = Salesforce(os.environ["SFCONSUMERKEY"], os.environ["SFCONSUMERSECRET"], domain=os.environ["SFDOMAIN"], refresh_token=os.environ.get("SFRFRESHTOKEN") or None)
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "contacts.csv"))
# Insert the contacts first, so that we can demonstrate upserting them.
df, _ = sf.insert(df, "Contact") 
# Also add 100 new contacts to the dataframe, so that we can demonstrate upserting them also
new_contacts = pd.DataFrame({
    "FirstName": "ForceBites",
    "LastName": [f"New contact {number}" for number in range(1, 101)],
})
df = pd.concat([df, new_contacts], ignore_index=True)
df["LastName"] = df["LastName"] + " (upserted)"
successful, failed = sf.upsert(df, "Contact", "Id")
print(successful)
print(failed)

# Clean up.
sf.delete(sf.query("SELECT Id FROM Contact WHERE FirstName = 'ForceBites'"), "Contact")
