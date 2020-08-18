from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://root:SuperSecret@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false')

print("Count all documents marked as \"inactive\" for demonstration purposes...")
result = client['tilt']['tilt'].count_documents(
  filter = { "meta.status" : "inactive"}
)
print(result)

print("Find all controllers that send data to \"Red\"...")
filter={
    'meta.status': 'inactive', 
    'dataDisclosed.recipients.name': 'Red'
}
project={
    'meta.name': 1, 
    '_id': 0
}

result = client['tilt']['tilt'].find(
  filter=filter,
  projection=project
)

for r in result:
  pprint(r)
