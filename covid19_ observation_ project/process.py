"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""

# - retrieve the total number of records that have been loaded

# import csv and tui module

import csv
from csv import reader
from csv import DictReader
import tui

# retrieve the total number of records that have been loaded:


def total_num_of_record():
    try:
        with open ("covid_19_data.csv") as file:
            csv_reader = csv.reader(file)
            headings = next(csv_reader)
            lines = len(list(csv_reader))
            print(f"Total of {lines} records have been loaded.")

    except IOError:
        tui.error("Enter valid file name")


#total_num_of_record()


# - Retrieve a record with the serial number as specified by the user:


def search_by_number():
    serial_number = int(input("Enter a serial number from 0 to 513: "))

    try:
        with open("covid_19_data.csv", "r") as read_obj:
            csv_reader = reader(read_obj)
            records = list(csv_reader)
            print(records[serial_number])
            if serial_number > 513:
                print("Please enter a valid serial number from 0 to 513: ")

    except ValueError:
        tui.error("Please enter a valid serial number from 0 to 513: ")


#search_by_number()


# - Retrieve the records for the observation dates as specified by the user:


def search_by_date():
    observation_date = str(input("Enter an observation date in the format MM/DD/YYYY: "))
    try:
        with open("covid_19_data.csv", "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if observation_date in row[1]:
                    print(row)

    except ValueError:
        tui.error("Please enter a valid observation date in the format MM/DD/YYYY ")


#search_by_date()


# - Retrieve all of the records grouped by the country/region:


def search_by_country():
    country_name = str(input("To search by country/region; enter a country_or_region name: ")).title()

    try:
        with open("covid_19_data.csv", "r") as file:
            csv_reader = csv.reader(file)
            print(f"The records for {country_name:} are: ")
            for row in csv_reader:
                if country_name in row[3]:
                    print(row)
    except IOError:
        tui.error("Please enter a valid country name ")


#search_by_country()


# - Retrieve all summary of all of the cases for each country/region:


def search_country_case():
    country_name = str(input("To search by cases. Please enter a country_or_region name: ")).title()

    try:
        with open("covid_19_data.csv", "r") as file:
            csv_reader = csv.reader(file)
            print(f"The total number of confirmed cases, deaths and recoveries for {country_name:} are: ")
            for row in csv_reader:
                if country_name in row[3]:
                    print(row[5:])
    except IOError:
        tui.error("Please enter a valid country name ")


#search_country_case()


if __name__ == "__main__":
    run()
