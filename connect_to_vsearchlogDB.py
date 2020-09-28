import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=CEPR_NSK_23\SQLEXPRESS01;'
                      'Database=vsearchlogDB;'
                      'Trusted_Connection=yes;')
