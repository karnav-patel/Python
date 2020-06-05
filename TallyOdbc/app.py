import pyodbc
import json
import numpy as np


conn = pyodbc.connect('DSN=TallyODBC64_9000;SERVER=({local});DRIVER=Tally ODBC DRIVER64;PORT=9000')

cursor=conn.cursor()

data=cursor.execute("SELECT $Name FROM Company")

columns = [column[0] for column in data.description]
actual_cols=[s.strip('$') for s in columns]
rows = data.fetchall()

print(rows)
