import os
import sqlite3
import pandas as pd

# data_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv'
# headers = ['patient_id','name','sex','age','phone','dob']
# data_table = pd.read_csv(data_url, header=None, names=headers, converters={'zip': str})

# Clear example.db if it exists
# if os.path.exists('hospital.db'):
#     os.remove('hospital.db')

# Create a database
conn = sqlite3.connect('hospital.db', check_same_thread=False)

# Add the data to our database
# data_table.to_sql('patients', conn, dtype={
#     'patient_id':'INT',
#     'name':'VARCHAR(30)',
#     'sex':'CHAR(1)',
#     'age':'INT',
# 	'phone':'INT',
# 	'dob':'DATE',
# })

conn.row_factory = sqlite3.Row

# Make a convenience function for running SQL queries
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_insert_edit_delete(query):
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()

def sql_any_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    names = rows[0].keys()
    print("hello",names)
    return names,rows

# def sql_delete(query,var):
#     cur = conn.cursor()
#     cur.execute(query,var)
#     conn.commit()

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows
