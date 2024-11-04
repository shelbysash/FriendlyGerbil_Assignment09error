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


#step 1    
query_string = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
#print(query_string)
#Submit the query to out db server and store the results in a variable
results = cursor.execute(query_string)
products = cursor.fetchall()  #maybe ?

#step 2
selectedProduct = random.choice(products)
productID = selectedProduct.ProductID
description = selectedProduct.Description
manufacturerID = selectedProduct.ManufacturerID
brandID = selectedProduct.BrandID