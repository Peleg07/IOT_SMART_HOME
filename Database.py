import sqlite3
from sqlite3 import Error
from datetime import datetime

#create new database
def CreateDatabase(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    if(conn):
        conn.commit()
        print("Database {} created successfully.".format(database))
        conn.close()
        print("Database connection is closed")
    else:
        print("Unable to create Database.")


#check connection to database\if database exist
def CheckDatabaseConnection(database):
    conn = sqlite3.connect(database)
    if(conn):
        print("Connected successfully to Underfloor Heating Database.")
    else:
        print("Unable to connect to Database.")
    conn.close()
    print("Database connection is closed")


#create new table for sensor/DHT
def CreateDatabaseTable_Sensor(database,tableName):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    create_query = '''CREATE TABLE {}(Sensor_timestamp TIMESTAMP,Temperature REAL,Humidity REAL)'''.format(tableName)
    cursor.execute(create_query)
    conn.commit()
    print("Table: {} has been created.".format(tableName))
    conn.close()
    print("Database connection is closed")

#create new table for Button
def CreateDatabaseTable_Button(database,tableName):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    create_query = '''CREATE TABLE {}(Button_timestamp TIMESTAMP,Button_Action INTEGER)'''.format(tableName)
    cursor.execute(create_query)
    conn.commit()
    print("Table: {} has been created.".format(tableName))
    conn.close()
    print("Database connection is closed")

#create new table for Relay
def CreateDatabaseTable_Relay(database,tableName):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    create_query = '''CREATE TABLE {}(Realy_timestamp TIMESTAMP,Realy_message TEXT)'''.format(tableName)
    cursor.execute(create_query)
    conn.commit()
    print("Table: {} has been created.".format(tableName))
    conn.close()
    print("Database connection is closed")

#delete exist table
def DeleteDatabaseTable(database,tableName):
    conn = sqlite3.connect(database)
    conn.execute("DROP TABLE {}".format(tableName))
    print("Table: {} deleted successfully".format(tableName))
    conn.commit()
    conn.close()


#insert data to table
def InsertToDatabase(database,tableName,value_1,value_2):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    # create query to insert the data
    insertQuery = """INSERT INTO {} VALUES (?, ?)""".format(tableName)
    cursor.execute(insertQuery, (value_1,value_2))
    conn.commit()
    print("Data inserted to table '{}' successfully".format(tableName))
    conn.close()
    print("Database connection is closed")


#insert data to sensor table
def InsertToDatabaseSensor(database,tableName,date,temperature,humidity):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    # create query to insert the data
    insertQuery = """INSERT INTO {} VALUES (?, ?, ?)""".format(tableName)
    cursor.execute(insertQuery, (date,temperature,humidity))
    conn.commit()
    print("Data inserted to table '{}' successfully".format(tableName))
    conn.close()
    print("Database connection is closed")


def GetDataFromTable(database,tableName):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT rowid,* FROM {}".format(tableName))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    print("Database connection is closed")


def DeleteRowFromTable(rowid,database):
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        print("Connected to {}".format(database))

        delete_query = """DELETE from Sensor_Temperature where rowid = ?"""
        cursor.execute(delete_query, (rowid,))
        conn.commit()
        print("Record ID: {} deleted successfully".format(rowid))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("Database connection is closed")


#variables
dateFromat = "%d-%m-%Y %H:%M:%S"
date = datetime.now().strftime(dateFromat)
database = "underfloor_heating.db"
tablename_1 = "Remote_Sensor"
tablename_2 = "Remote_BUTTON"
tablename_3 = "Remote_RELAY"
temperature = 28
#tableQuery = '''CREATE TABLE Sensor(Sensor_timestamp TIMESTAMP,Temperature INTEGER)'''


#CheckDatabaseConnection(database)
#InsertToDatabase(database,tablename_1,date,temperature)
#GetDataFromTable(database,tablename_3)
#print(currentDateTime)
#DeleteRowFromTable(1,database)
#CreateDatabaseTable_Sensor(database,tablename_1)
#CreateDatabaseTable_Button(database,tablename_2)
#CreateDatabaseTable_Relay(database,tablename_3)
#DeleteDatabaseTable(database,tablename_3)




