"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import read_query, update_query, delete_query, sorting_Change


# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query
print("Querying data...")
read_query()
update_query()
delete_query()
sorting_Change()
