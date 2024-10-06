"""
This module is responsible for setting up and querying the database.
"""

"""
Task 22 - 26: Write suitable functions to query the database as follows:

Setup database
Retrieve the names of all (unique) countries in alphabetical order
Retrieve the number of confirmed cases, deaths and recoveries for a specified observation / serial number.
Retrieve information for the top 5 countries for confirmed cases
Retrieve information for the top 5 countries for death for specific observation dates


The function for setting up the database should do the following:
- Take a list of records as a parameter
- Use the list passed as a parameter value to create and populate a suitable database. You are required to design a
suitable (small) database.
- It is recommended that you complete this function last and start by creating your database using a tool such as
SQL DB Browser. This would allow you to complete the other database functions first.  You can then complete this
function to generate the database via code.

Each function for querying the database should follow the pattern below:
- Take no parameters
- Query the database appropriately. You may use the module 'tui' to retrieve any additional information 
required from the user to complete the querying.
- Return a list of records as retrieved from the database

"""

# importing sqlite 3

import sqlite3
import tui

# define connection and cursor

db = sqlite3. connect("Com728 database.db")

cursor = db.cursor()

# insert into cases table

sql2 = """
INSERT INTO cases(serial_number, observation_date, update_time, confirmed_cases, deaths, recovered)
VALUES
(450, "01/31/2020", "23:59", 5806, 204, 141),
(485, "01/31/2020", "23:59", 15, 0, 1),
(318, "01/28/2020", "23:00" , 14, 0, 6),
(486, "01/31/2020", "23:59", 13, 0, 0),
(479, "01/31/2020", "23:59", 12, 0, 0),
(487, "01/31/2020", "23:59", 11, 0, 0),
(480, "1/31/2020", "23:59", 10,0,0),
(390, "01/30/2020", "16:00", 4903, 162, 90),
(280, "01/28/2020", "23:00", 3554, 125, 80),
(334, "01/29/2020", "19:30", 3554, 125, 88),
(227, "01/27/2020", "23:59", 1423, 76, 45),
(178, "01/26/2020", "16:00", 1058, 52, 42);
"""

#cursor.execute(sql2)

#db.commit()


# insert into province_state table

sql2 = """ 
INSERT INTO provinces_or_states(country_or_region_id, case_serial_number, province_or_state_name)
VALUES
(16, 450, "Hubei"),
(13, 485, " "),
(24, 318, " "),
(21, 486, " "),
(10, 479, "Hong Kong"),
(22, 487, " "),
(29, 480, "Taiwan"),
(16, 390, "Hubei"),
(16, 280, "Hubei"),
(16, 334, "Hubei"),
(16, 227, "Hubei"),
(16, 178, "Hubei");
"""

#cursor.execute(sql2)

#db.commit()

# retrieve the names of all (unique) countries in alphabetical order


def read_country_from_db():
    country_query = """
                    SELECT id, country_or_region
                    FROM countries_or_regions
                    ORDER BY country_or_region ASC
                    """
    cursor.execute(country_query)
    unique_row = cursor.fetchall()
    print(" *****The names of all the (unique) countries in alphabetical order are: *****")
    for row in unique_row:
        print(row)


#read_country_from_db()


# retrieve the number of confirmed cases, deaths and recoveries for a specified observation / serial number

def read_country_cases_db():
    country_cases_query ="""
                        SELECT observation_date, serial_number, confirmed_cases, deaths, recovered 
                        FROM cases 
                        WHERE observation_date >='01/25/2020' AND serial_number >=166
                        """

    cursor.execute(country_cases_query)
    query_row = cursor.fetchall()
    print(""" ***** The number of confirmed cases, deaths and recoveries for observation_date >= '01/25/2020'
    AND serial_number >=166 are: ***** """)
    for row in query_row:
        print(row)


#read_country_cases_db()


# retrieve top 5 countries for confirmed cases

def top_confirmed_cases_db():
    top_confirmed_query = """
                        SELECT country_or_region, confirmed_cases FROM countries_or_regions
                        INNER JOIN provinces_or_states ON provinces_or_states.country_or_region_id = countries_or_regions.id 
                        INNER JOIN cases ON cases.serial_number = provinces_or_states.case_serial_number
                        WHERE "confirmed_cases" = 5806 OR "confirmed_cases" <=15
                        ORDER BY cases.confirmed_cases DESC 
                        LIMIT 5
                        """

    cursor.execute(top_confirmed_query)

    output = cursor.fetchall()
    print("*****The top 5 countries for confirmed cases are: ******")
    for item in output:
        print(item)


#top_confirmed_cases_db()


# retrieve top 5 countries for deaths

def top_deaths_db():
    top_deaths_query = """
                    SELECT observation_date, country_or_region, deaths FROM countries_or_regions
                    INNER JOIN provinces_or_states ON provinces_or_states.country_or_region_id = countries_or_regions.id 
                    INNER JOIN cases ON cases.serial_number = provinces_or_states.case_serial_number
                    WHERE observation_date >="01/22/2020" AND deaths >0
                    ORDER BY deaths DESC
                    LIMIT 5
                    """
    cursor.execute(top_deaths_query)

    output = cursor.fetchall()
    print("*****The top 5 countries for deaths for specific observation dates are: ******")
    for item in output:
        print(item)


#top_deaths_db()



if __name__ == "__main__":
    run()





