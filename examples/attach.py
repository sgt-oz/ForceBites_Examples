"""attach(): attach a file to each row's record, as a classic Attachment.

Inserts 1,000 of the made-up Contacts in data/contacts.csv, attaches data/hello.txt to each one, then
deletes the attachments and the Contacts again.

To run it (steps 1 and 2 are only needed once):
    1. pip install forcebites python-dotenv
    2. Copy .env.example to .env, both in the repo folder, and fill in your connected app's details.
    3. python examples/attach.py
"""

import os
import pandas as pd
from dotenv import load_dotenv
from forcebites import Salesforce

load_dotenv()
sf = Salesforce(os.environ["SFCONSUMERKEY"], os.environ["SFCONSUMERSECRET"], domain=os.environ["SFDOMAIN"], refresh_token=os.environ.get("SFRFRESHTOKEN") or None)
contacts = pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "contacts.csv")).head(1000)
# Insert the contacts first, so that we can demonstrate attaching files to them.
contacts, _ = sf.insert(contacts, "Contact")  
df = pd.DataFrame({
    "ParentId": contacts["Id"],  
    "Path": os.path.join(os.path.dirname(__file__), "data", "hello.txt"),  # the file on disk
})
successful, failed = sf.attach(df)
print(successful)
print(failed)

# Clean up. 
sf.delete(successful, "Attachment")
sf.delete(sf.query("SELECT Id FROM Contact WHERE FirstName = 'ForceBites'"), "Contact")
