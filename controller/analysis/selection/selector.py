import pandas as pd
import pandas.io.sql as pdsql
import datetime

def dateSelector (trxn):
    minSelectRepeat = True
    maxSelectRepeat = True

    while(minSelectRepeat):
        user_input = input("Enter the lower bound date from " + trxn.Date.min().strftime("%Y-%m-%d") + " in format \"YYYY-MM-DD\".\n")
        user_min = datetime.datetime.strptime(user_input, "%Y-%m-%d").date()
        if (user_min >= trxn.Date.min()):
            minSelectRepeat = False
            print("Lower bound: " + datetime.date.strftime(user_min))
            while (maxSelectRepeat):
                user_input = input("Enter the upper bound date to " + trxn.Date.max().strftime("%Y-%m-%d") + " in format \"YYYY-MM-DD\".\n")
                user_max = datetime.datetime.strptime(user_input, "%Y-%m-%d").date()
                if (user_max <= trxn.Date.max()):
                    print("Upper bound: " + datetime.date.strftime(user_max))
                    maxSelectRepeat = False
                else:
                    print("Please choose a date ≤ " + trxn.Date.max().strftime("%Y-%m-%d") + "\n")
        else:
            print("Please choose a date ≥ " + trxn.Date.min().strftime("%Y-%m-%d") + "\n")
    return trxn[(trxn.Date >= min) & (trxn.Date <= max)]

def categorySelector (trxn):
