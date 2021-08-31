"""
Convert the CSV to JSON
A CSV file named q3_candidates.csv is attached. The file has the following headers:
id - integer, name - string, email - string, phone - string, degree - string, major - string, institute - string
title - string, company - string

skills - list of lowercase strings

1. Load the data from the CSV into a Python data structure and then print them.

2. Make sure you load data into proper data structures and data types.
Example:
- id must be an integer.
- “skills” is a list of lowercase strings. "Python,Django, Tensorflow" should
be converted to [“python”, ”django”, “tensorflow”].

3. Then store this data into a JSON file named “q3_candidates_processed.json”.

4. NOTE:
- Structure your code into appropriate functions.
- Make sure you don’t hard-code the file paths of the CSV and JSON files. Use
relative paths instead.
- Don’t use any third party libraries like Pandas.

5. HINT:
- Store the data in a list of dictionaries where each item represents a row from the
CSV."""

import csv
import json
import os


# format the skills as required
import time


def formatting(data=None):
    if data is None:
        data = []

    for rows in csv_reader:
        # store in list of dictionaries
        data.append(dict(zip(keys, rows)))
    for candidate in data:
        if 'skills' in candidate.keys():
            candidate['skills'] = candidate['skills'].lower()
            candidate['skills'] = candidate['skills'].replace(" ", "")
    return data


# read csv data
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "q3_candidates.csv")

with open(os.path.join(path), "r") as f:
    csv_reader = csv.reader(f)
    csv_reader = list(csv_reader)
    keys: object = csv_reader[0]
    csv_reader.pop(0)

# call formatting function
csv_data = formatting()
print("\nReading CSV data...... ")

time.sleep(2)

# dump to json
with open(os.path.join(path), "w") as f:
    json.dump(csv_data, f, indent=2)
    print("\nData dumped to the json file Successfully!")
