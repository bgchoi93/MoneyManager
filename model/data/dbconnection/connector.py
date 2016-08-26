import pymysql;

def InitializeConnection (host_name, port_number, user_name, password) :
    conn = pymysql.connect(host = host_name, port = port_number, user= user_name, passwd = password, db='moneymanagerdb');
    return conn;

def ExecuteQuery () :
    return null;