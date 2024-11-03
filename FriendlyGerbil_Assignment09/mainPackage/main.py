#main

from dbUtilitiesPackage.dbUtilities import *

import pyodbc
try:
    conn= connect_to_database() 
    # Submit a query to the SQL Server instance and store the results in the cursor object
    cursor = conn.cursor()  #establishes temporary table 
    cursor.execute('SELECT * FROM tAmericanAthleticConference') #submits sql to db engine and stores in cursor
except Exception as e: 
    #I'd like to know more
    print("error accessing database")
    print(e) 
    exit()  #given up. how do i get out of this module 
