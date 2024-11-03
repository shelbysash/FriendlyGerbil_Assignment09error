#db utilities

import pyodbc

def connect_to_database():
    """
    Connect to the database
    @return Connecition Object: the open connection, or None on error
    """
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=lcb-sql.uccob.uc.edu\\nicholdw;' #added 'x' for error
                              'Database=IS4010;'
                              'uid=IS4010Login;'
                              'pwd=P@ssword2;')  #added 'a' to end of this password to make error
    except: 
        conn = None  #failture 
        
    return conn
