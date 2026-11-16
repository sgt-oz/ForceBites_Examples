"""query(): run a SOQL query and get every matching row back as a pandas DataFrame.

To run it (steps 1 and 2 are only needed once):
    1. pip install forcebites python-dotenv
    2. Copy .env.example to .env, both in the repo folder, and fill in your connected app's details.
    3. python examples/query.py
"""

import os
from dotenv import load_dotenv
from forcebites import Salesforce

load_dotenv()
sf = Salesforce(os.environ["SFCONSUMERKEY"], os.environ["SFCONSUMERSECRET"], domain=os.environ["SFDOMAIN"], refresh_token=os.environ.get("SFRFRESHTOKEN") or None)
df = sf.query("SELECT Id, Name FROM Contact LIMIT 1000000")
print(df)
