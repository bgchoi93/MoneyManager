import sys
sys.path.append('~/Documents/Project/MoneyManager')
import model.data.dbconnection.connector as dbconn
import pandas.io.sql as pdsql
import model.data.data_import.csv_reader as csvreader

if __name__ == "__main__":
    cnxn = dbconn.InitializeConnection("localhost", 3306, "moneymanager", "")
    cursor = cnxn.cursor()
    repeat = True
    while (repeat):
        print("Choose an option: ")
        print("1. Import Data\n2. Analyze consumption\n3. Quit\n4. Test")
        user_input = input()
        if (user_input == "3"):
            repeat = False
        else:
            if(user_input == "1"):
                print("Selected: Import Data")
                csvreader.reader(cnxn, cursor)
            elif(user_input == "2"):
                print("Analyze")
            elif(user_input == "4"):
                sql = input("Enter query: ")
                query_result = pdsql.read_sql(sql, cnxn)
                print(query_result)
            else:
                print("Wrong Input!")


