![Python application](https://github.com/Transparency-Information-Language/tilt-sample-analysis/workflows/Python%20application/badge.svg?event=push)

# tilt Sample Analysis tasks
In this repository it is shown how potential analysis tasks could be performed using [python-tilt](https://github.com/Transparency-Information-Language/python-tilt) and the [tilt-hub](https://github.com/Transparency-Information-Language/tilt-hub).

## Usage

```bash
# In order to install all necessary dependencies
pip install -r requirements.txt

    Collecting requests==2.22.0
    Downloading requests-2.22.0-py2.py3-none-any.whl (57 kB)
        |████████████████████████████████| 57 kB 1.2 MB/s
    ...
    ...
    ...

# Insert dummy content into the local MongoDB
python3 sample-inserter.py

    Cleaning inactive documents...
    <pymongo.results.DeleteResult object at 0x10457fc80>
    Inserting sample documents...
    <pymongo.results.InsertOneResult object at 0x10459abc0>
    <pymongo.results.InsertOneResult object at 0x1042cb240>
    <pymongo.results.InsertOneResult object at 0x10457fd40>
    <pymongo.results.InsertOneResult object at 0x1045bcb80>
    <pymongo.results.InsertOneResult object at 0x1045bcb40>
    <pymongo.results.InsertOneResult object at 0x10432a040>
    <pymongo.results.InsertOneResult object at 0x103d24440>

# Perform sample queries 
python3 sample-query.py

    Count all documents marked as "inactive" for demonstration purposes...
    7
    Find all controllers that send data to "Red"...
    {'meta': {'name': 'Blue'}}
    {'meta': {'name': 'Yellow'}}
````

## Author
Elias Grünewald

## License
GNU General Public License, Version 3
