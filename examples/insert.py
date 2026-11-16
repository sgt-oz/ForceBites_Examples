"""insert(): create a new record for each row of a DataFrame.

Creates the 5,000 made-up Contacts in data/contacts.csv, all with the first name "ForceBites", then
deletes them again. 

To run it (steps 1 and 2 are only needed once):
    1. pip install forcebites python-dotenv
    2. Copy .env.example to .env, both in the repo folder, and fill in your connected app's details.
    3. python examples/insert.py
"""

import os
import pandas as pd
from dotenv import load_dotenv
from forcebites import Salesforce

load_dotenv()
sf = Salesforce(os.environ["SFCONSUMERKEY"], os.environ["SFCONSUMERSECRET"], domain=os.environ["SFDOMAIN"], refresh_token=os.environ.get("SFRFRESHTOKEN") or None)
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "contacts.csv"))
successful, failed = sf.insert(df, "Contact")
print(successful)
print(failed)

# Clean up. 
sf.delete(sf.query("SELECT Id FROM Contact WHERE FirstName = 'ForceBites'"), "Contact")
