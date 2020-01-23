import pyodbc
class DataBaseConfig:

    def __init__(self,dbname):
        global cnxn
        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=LAPTOP-S1LVCJIH\SQLEXPRESS;"
                              "Database="+dbname+";"
                              "Trusted_Connection=yes;")
        print("DB Connected Successfully with the database "+dbname)
    def getLogin_Details(self):
        sqlQuery = "insert into tbl_phones_list values('{0}',{1})"
        cursor = cnxn.cursor()
        cursor.execute(sqlQuery)
        for row in cursor:
            print(row)








