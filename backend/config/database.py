import cx_Oracle

USERNAME = "soil_user"
PASSWORD = "soil123"
DSN = cx_Oracle.makedsn("oracle", 1521, service_name="freepdb1")

def get_connection():
    return cx_Oracle.connect(USERNAME, PASSWORD, DSN)