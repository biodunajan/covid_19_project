"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, querying of the database and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any database related querying should be done using the appropriate functions the module 'database'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""


# Task 10: Import required modules

import csv
import tui
import process
import database
import visual

# Task 11: Create an empty list named 'covid_records'.
# This will be used to store the data read from the source data file.

covid_records = []


def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.

    tui.welcome()

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should be a record in the list 'covid_records'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many records have
    # been loaded and that the data loading operation has completed.

    tui.progress("Data loading operation", 0)
    try:
        with open("covid_19_data.csv", "r") as file:
            csv_reader = csv.reader(file)
            headings = next(csv_reader)
            for row in csv_reader:
                covid_records.append(row)
                print(row)

    except IOError:
        tui.error("file cannot be found or loaded")

    num_record = (len(covid_records))
    tui.total_records({num_record})

    tui.progress("Data loading operation", 100)

    while True:
        # Task 14: Using the appropriate function in the module 'tui', display a menu of options
        # for the different operations that can be performed on the data (menu variant 0).
        # Assign the selected option to a suitable local variable

        choice = tui.menu

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an individual record by serial number then
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the record and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve (multiple) records by observation dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve records with
        #       - Use the appropriate function in the module 'tui' to display the retrieved records.
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group records by country/region then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the records
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the records then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the records.
        #       - Use the appropriate function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.

        tui.progress("Data processing operation", 0)

        tui.progress("Records retrieval by serial_number: ", 0)
        process.search_by_number()
        tui.progress("Records retrieval by serial_number: ", 100)

        tui.progress("Records retrieval by observation_date: ", 0)
        process.search_by_date()
        tui.progress("Records retrieval by observation date: ", 100)

        tui.progress("Records retrieval grouped by the country/region: ", 0)
        process.search_by_country()
        tui.progress("Records retrieval grouped by the country/region: ", 100)

        tui.progress("Records retrieval summary of all of the cases for each country/region: ", 0)
        process.search_country_case()
        tui.progress("Records retrieval summary of all of the cases for each country/region: ", 100)

        # Task 21: Check if the user selected the option for setting up or querying the database.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # database querying operation has started.
        # - Query the database by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what querying is to be done.
        #   - call the appropriate function in the module 'database' to retrieve the results
        #   - call the appropriate function in the module 'tui' to display the results
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # database querying operation has completed.

        tui.progress("database querying operation: ", 0)

        tui.progress("database querying operation by country: ", 0)
        database.read_country_from_db()
        tui.progress("database querying operations by country : ", 100)

        tui.progress("database querying operation by country's cases: ", 0)
        database.read_country_cases_db()
        tui.progress("database querying operations by country's cases : ", 100)

        tui.progress("database querying operation by top 5 confirmed cases: ", 0)
        database.top_confirmed_cases_db()
        tui.progress("database querying operation by top 5 confirmed cases: ", 100)

        tui.progress("database querying operation by top 5 deaths: ", 0)
        database.top_deaths_db()
        tui.progress("database querying operation by top 5 deaths: ", 100)

        # Task 27: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual'
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.

        tui.progress("Data visualization operation: ", 0)

        tui.progress("Piechart of top 5 countries for confirmed cases: ", 0)
        visual.pie_graph()
        tui.progress("Piechart of top 5 countries for confirmed cases: ", 100)

        tui.progress("Barchart of top 5 countries for confirmed cases: ", 0)
        visual.pie_graph()
        tui.progress("Barchart of top 5 countries for confirmed cases: ", 100)

        tui.progress("Animated visualisation of confirmed cases, deaths and recovery: ", 0)
        visual.draw_frame(frame_number=5)
        tui.progress("Animated visualisation of confirmed cases, deaths and recovery: ", 100)

        # Task 31: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop

        if choice == 4:
            break

        # Task 32: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message

        else:
            tui.error("Please enter a valid menu from 0 to 3: ")



if __name__ == "__main__":
    run()
