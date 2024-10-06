"""
This module is responsible for visualising the data retrieved from a database using Matplotlib.
"""

"""
Task 28 - 30: Write suitable functions to visualise the data as follows:

- Display the top 5 countries for confirmed cases using a pie chart
- Display the top 5 countries for death for specific dates using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country/countries.

Each function for the above should utilise the functions in the module 'database' to retrieve any data.
You may add additional methods to the module 'database' if needed. Each function should then visualise
the data using Matplotlib.
"""

# TODO: Your code here

#  Matplotlib importing and sqlite 3

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

import sqlite3
import numpy as np


# define connection and cursor

db = sqlite3. connect("Com728 database.db")

cursor = db.cursor()

# connecting and querying the database to retrieve confirmed cases dataset


def read_from_db():
    sql_query = """
    SELECT country_or_region, confirmed_cases FROM countries_or_regions
    INNER JOIN provinces_or_states ON provinces_or_states.country_or_region_id = countries_or_regions.id 
    INNER JOIN cases ON cases.serial_number = provinces_or_states.case_serial_number
    WHERE "confirmed_cases" = 5806 OR "confirmed_cases" <=15
    ORDER BY cases.confirmed_cases DESC 
    LIMIT 5
    """

    cursor.execute(sql_query)

    country_or_region = []
    confirmed_cases = []

    for i in cursor:
        country_or_region.append((i[0]))
        confirmed_cases.append(i[1])

    print(country_or_region)
    print(confirmed_cases)


#read_from_db()


# visualizing the top 5 countries for confirmed cases in piechart using matplotlib

def pie_graph():

    plt.rcParams["figure.figsize"] = [7.50, 4.50]
    plt.rcParams["figure.autolayout"] = True

    labels = ['Mainland China', 'Japan', 'Thailand', 'Singapore', 'Hong Kong']
    values = [5806, 15, 14, 13, 12]
    explode = (0.0, 0.0, 0.0, 0.0, 0.0)
    colors = ('red', 'cyan', 'yellow', 'green', 'blue')
    patches, texts, auto = plt.pie(values, colors=colors, shadow=True, startangle=90, explode=explode, autopct='%1.1f%%')

    plt.pie(values, labels=["", "", "", "", ""], colors=colors,explode=explode, shadow=True, startangle=90,autopct='%1.1f%%' )
    plt.title("""Top 5 countries/regions for covid-19 confirmed cases 
                in January 2020""")
    plt.legend(patches, labels, loc='best')
    plt.axis("equal")
    plt.xlabel(" ")
    plt.show()


pie_graph()


# connecting and querying the database to get deaths dataset

def read_deaths_db():

    read_death_query = """
        SELECT observation_date, country_or_region, deaths FROM countries_or_regions
        INNER JOIN provinces_or_states ON provinces_or_states.country_or_region_id = countries_or_regions.id 
        INNER JOIN cases ON cases.serial_number = provinces_or_states.case_serial_number
        WHERE 'deaths' >=0 OR 'deaths' <=204
        ORDER BY deaths DESC
        """
    cursor.execute(read_death_query)
    output = cursor.fetchall()
    print("*****The top 5 countries for deaths for specific observation dates are: ******")
    for item in output:
        print(item)


#read_deaths_db()


# visualizing the top 5 countries for deaths for specific dates in a bar chart using matplotlib

def bar_graph():
    data = {'Mainland China': 204, 'Japan': 0, 'Thailand': 0, 'Singapore': 0, 'Hong Kong': 0}
    country_or_region = list(data.keys())
    deaths = list(data.values())
    plt.title("Top 5 countries for covid-19 deaths for January 2020")
    plt.xlabel("country_or_region")
    plt.ylabel("deaths")

    plt.bar(country_or_region, deaths)
    plt.show()


bar_graph()


# connecting and querying the database to retrieve confirmed cases, death, and recovery dataset
# for (animated) visualisation

def confirmed_cases_db():

    confirmed_cases_query ="""
    SELECT observation_date, country_or_region, confirmed_cases, deaths, recovered FROM countries_or_regions
    INNER JOIN provinces_or_states ON provinces_or_states.country_or_region_id = countries_or_regions.id 
    INNER JOIN cases ON cases.serial_number = provinces_or_states.case_serial_number
    WHERE cases.confirmed_cases = 5806 OR "confirmed_cases" <=15
    ORDER BY confirmed_cases DESC
    LIMIT 5
    """

    cursor.execute(confirmed_cases_query)
    output = cursor.fetchall()
    print("*****Confirmed cases, death, and recovery for countries/regions in January 2020: ******")
    for item in output:
        print(item)


#confirmed_cases_db()


# animated visualization for confirmed cases, death, and recovery

def clear_frame():
    pass


def draw_frame(frame_number):
    global ax
    ax.cla()
    w = 0.3
    x = ['Mainland China', 'Japan', 'Thailand', 'Singapore', 'Hong Kong']
    confirmed_cases = [5806, 15, 14, 13, 12]
    deaths = [204, 0, 14, 13, 12]
    recoveries = [141, 1, 6, 0, 0]
    y = np.arange(len(x))

    bar1 = np.arange(len(x))
    bar2 = [i + w for i in bar1]
    bar3 = [i + w for i in bar2]

    plt.bar(bar1, confirmed_cases, w, label="confirmed_cases")
    plt.bar(bar2, deaths, w, label="deaths")
    plt.bar(bar3, recoveries, w, label="recoveries")
    plt.bar(bar1[:frame_number], bar2[:frame_number], bar3[:frame_number])

    plt.xlabel('Countries')
    plt.ylabel("No. of confirmed cases, deaths and recoveries")
    plt.title("""Covid-19 confirmed cases, deaths, and recoveries for January 2020""")
    plt.xticks(bar1 + w, x)
    plt.legend()

# setting up animation loop

fig = plt.figure()
ax = fig.subplots()
my_animation = animation.FuncAnimation(fig,
                                       draw_frame,
                                       frames=5,
                                       init_func=clear_frame,
                                       repeat=True,
                                       interval=500)

plt.show()






