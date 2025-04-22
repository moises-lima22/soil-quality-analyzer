import cx_Oracle

USERNAME = "soil_user"
PASSWORD = "soil123"
DSN = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")

def get_connection():
    return cx_Oracle.connect(USERNAME, PASSWORD, DSN)