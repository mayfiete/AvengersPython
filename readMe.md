
# Avengers Python Project

** This is a project to fetch data from an API and store it in a database. The data is then pivoted to a more readable format. **

##  Sequence of commands
    1: fetch_heroes.py
    2: format_json.py
    3: persist.py
    4: pivot_db_data.py
    5: write_to_mongdb.py 
    6: rate_heroes.py
OR 
    script_runner.py

##  Overview of Scripts
    * DbConnx.py: contains the class DbConnx which is used to connect to the database
    * fetch_heroes.py: fetches the data from the API and stores it in a json file
    * format_json.py: formats the json file to a more readable format
    * persist.py: persists the data into the database
    * pivot_db_data.py: pivots the data from the database to a more readable format
    * message_broker.py: message broker - connecting Python to rabbitmq
    * write_to_mongoddb.py: copy data from csv into mongodb

** Database migrations managed using Flyway ** 
