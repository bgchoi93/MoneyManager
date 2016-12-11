import controller.analysis.selection.selector as selector
import pandas as pd
import pandas.io.sql as pdsql
import numpy
import

def analysisSelector (cnxn, cursor) :
    repeat = True
    while (repeat):
        print("Choose an anlaysis: ")
        print("1. Distribution \n2. Aggregation \n3. Back to Main Menu")
        user_input = input()
        if (user_input == "1"):
            print("Selected Distribution.")
            distribution(cnxn, cursor)
        elif (user_input == "2"):
            print("Selected Aggregation.")
        elif (user_input == "3"):
            repeat = False
        else:
            print("Wrong Input!")

def distribution (conn, cursor) :
    transaction = pdsql.read_sql("select Account.Description as Account, Description.Category as Category, Amount, Date, Balance, case when Amount < 0 then \'Out\' else \'In\' end as Type from Transaction inner join Description on Transaction.Description = Description.Id inner join Account on Transaction.Account = Account.Id", conn)
    transaction = selector.dateSelector(transaction)

    dist = transaction.groupby(['Type', 'Category']).sum()['Amount']
    distByCategory = transaction.groupby('Category').sum()['Amount']
    distByType = transaction.groupby('Type').sum()['Amount']

    print("View Distribution analysis over: ")
    print("1.Overall \n2. Category \n3. Income/Consumption \n4.Quit")
    user_input = input()
    if (user_input == "1"):

    elif (user_input == "2"):

    elif (user_input == "3"):

    elif (user_input == "4"):
    else:
