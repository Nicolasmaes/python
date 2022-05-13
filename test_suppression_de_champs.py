import os
import http.client
import json
import csv
import pandas
from datetime import datetime


def read_json(filename: str) -> dict:

    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")

    return data


def create_dataframe(data: list) -> pandas.DataFrame:

    # Declare an empty dataframe to append records
    dataframe = pandas.DataFrame(columns=[
        "type",
        "id",
        "identification.login",
        "identification.passwordExpiration",
        "identity.gender",
        "identity.firstName",
        "identity.lastName",
        "identity.email",
        "status.validated",
        "activity.creationDate",
        "activity.lastUpdateDate",
        "cgu.acceptation.version",
        "cgu.acceptation.date",
        "preferences.cultureName",
        "preferences.date.utc",
        "preferences.date.format.type",
        "preferences.date.format.value",
        "preferences.actionStateAlert",
        "preferences.timeZone.type",
        "preferences.timeZone.name",
        "parent"
])

    # Looping through each record
    for d in data:
        
        # Normalize the column levels
        record = pandas.json_normalize(d)
        
        # Append it to the dataframe
        dataframe = dataframe.append(record, ignore_index=False)

    return dataframe


def main():
    # Read the JSON file as python dictionary
    data = read_json(filename="test_suppression_de_champs.json")

    # Generate the dataframe for the array items in
    # details key
    dataframe = create_dataframe(data=data['data'])
    
    
     # Convert dataframe to CSV
    dataframe.to_csv("test_suppression_de_champs.csv", index=False,header=True,line_terminator="\n")

if __name__ == '__main__':
     main()