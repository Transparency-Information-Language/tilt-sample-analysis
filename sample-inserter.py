from tilt import tilt
import json
import requests
from pymongo import MongoClient
from pprint import pprint

client = MongoClient(
    'mongodb://root:SuperSecret@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false')

print('Cleaning inactive documents...')
clean = client['tilt']['tilt'].delete_many({"meta.status": "inactive"})
print(clean)

companies = [
    {'name': 'Blue', 'recipients': ['Red', 'Green']},
    {'name': 'Red', 'recipients': ['Yellow']},
    {'name': 'Green', 'recipients': ['Yellow']},
    {'name': 'Yellow', 'recipients': ['Red']},
    {'name': 'White', 'recipients': ['Orange']},
    {'name': 'Black', 'recipients': ['Orange']},
    {'name': 'Orange', 'recipients': ['Purple']},
]

# Use this document as a template
file = requests.get(
    'https://raw.githubusercontent.com/Transparency-Information-Language/schema/master/tilt.json')

print('Inserting sample documents...')
for c in companies:
    t = tilt.tilt_from_dict(json.loads(file.content))
    t.meta.name = c['name']
    t.meta.status = 'inactive'
    t.data_disclosed[0].recipients = []
    for r in c['recipients']:
        recipient = tilt.Recipient(
            name=r, address='', category='', country='', division='', representative=None)
        t.data_disclosed[0].recipients.append(recipient)

    # Insert to MongoDB
    result = client['tilt']['tilt'].insert_one(
        t.to_dict()
    )
    print(result)