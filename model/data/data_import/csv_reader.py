import pandas as pd
import pandas.io.sql as pdsql
import numpy as np

def reader (conn, cursor) :
    activity_type = input("Choose an activity type: \n1. Debit\n2.Credit\n")
    file_path = input("Enter a path to the file: ")

    raw_data = pd.read_csv(file_path, names = ['Date', 'Description', 'Out', 'In', 'Balance'], parse_dates=True)
    if (activity_type == "2"):
        raw_data['Balance'] *= -1
    raw_data['Out'] *= -1
    raw_data['Date'] = pd.to_datetime(raw_data['Date'], format='%m/%d/%Y')
    print("\nData: \n")
    print(raw_data)

    accountId = account_selector(conn, cursor)

    for index, entry in raw_data.iterrows():
        feed_entry(conn, cursor, accountId, entry)

    print("---------------------------------------------------------------------------\n" + "Importing data is completed. \n---------------------------------------------------------------------------\n")

def account_selector (conn, cursor):
    print("---------------------------------------------------------------------------\n" + "Select Account: ")
    accounts = pdsql.read_sql('SELECT * FROM Account', conn)
    account_list = []
    i = 1
    for index, account in accounts.iterrows():
        print(str(i) + '. ' + account['Description'])
        account_list.append(account)
        i += 1
    selection = input()
    account_selected = account_list[int(selection)-1]['Id']
    print("Selected " + account_selected)
    return account_selected

def category_creator (conn, cursor, description):
    repeat = True
    while (repeat):
        categoryId = input("Enter Category Id: ")
        categoryDescription = input("Enter Category Detail: ")
        response = input("Entering " + categoryId + ' - ' + categoryDescription + '. \nIs this information correct? (Y/N) : ')
        if (response == "Y"):
            repeat = False
    insert_sql = "INSERT INTO Category VALUES" + "(\'" + categoryId + "\', \'" + categoryDescription + "\')"
    cursor.execute(insert_sql)
    conn.commit()
    print("Created New Category.")
    return categoryId

def category_selector (conn, cursor, description):
    descriptions = pdsql.read_sql('SELECT Id FROM Description WHERE Id = \'' + description + '\'', conn)
    if (descriptions.empty):
        print("---------------------------------------------------------------------------\n" + description + ": ")
        categories = pdsql.read_sql('SELECT * FROM Category', conn)
        if (categories.empty):
            print("There is no category defined. Please create a new category")
            categoryId = category_creator(conn, cursor, description)
        else:
            print("There is no matching category for this description. Select a category: ")
            category_list = []
            i = 1
            for index, category in categories.iterrows():
                print(str(i) + '. ' + category['Id'] + ' - ' + category['Detail'])
                category_list.append(category)
                i += 1
            print(str(i) + '. ' + 'Not listed above. Create a new Category.')
            selection = input()
            if (selection == str(i)):
                categoryId = category_creator(conn, cursor, description)
            else:
                categoryId = category_list[int(selection)-1]['Id']
        insert_sql = "INSERT INTO Description VALUES " + "(\'" + description + "\', \'" + categoryId + "\')"
        cursor.execute(insert_sql)
        conn.commit()
        print("Selected " + description + ": " + categoryId + ".")

def feed_entry (conn, cursor, accountId, entry) :
    category_selector(conn, cursor, entry['Description'])
    descriptionId = entry['Description']
    if(np.isnan(entry['In'])):
        amount = entry['Out']
    else:
        amount = entry['In']
    date = entry['Date']
    balance = entry['Balance']

    insert_sql = "INSERT INTO Transaction VALUES " + "(UUID(), \'" + accountId + "\', \'" + descriptionId + "\', " + str(amount) + ", \'" + str(date) + "\', " + str(balance) + ")"
    cursor.execute(insert_sql)
    conn.commit()
