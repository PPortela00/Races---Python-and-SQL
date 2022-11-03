import pandas as pd
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import psycopg2
from load_races import con

def menu():
    print('\n')
    print("[1] ")
    print("[2]  ")
    print("[3]  ")
    print("[4] ")
    print("[5] ")
    print("[6] ")
    print("[7] ")
    print("[8] ")
    print("[9] ")
    print("[10] ")
    print("---------------------------5 Questions ---------------------------")
    print("[11] Who run the fastest 10K race ever (name, birthdate, time)")
    print("[12] What 10K race had the fastest average time (event, event date)?")
    print("[13] What teams had more than 3 participants in the 2016 maratona (team)?")
    print("[14] What are the 5 runners with more kilometers in total (name, birthdate, kms)?")
    print("[15] What was the best time improvement in two consecutive maratona races (name,birthdate, improvement)?")
    print("[16] What was the best time improvement in two consecutive maratona races (name,birthdate, improvement)?")

    print("[0] Exit the program.")

menu()
option = int(input("Insert the command that you want to execute:\n"))

while option != 0:
    if option == 1:
        id = int(input('Employee ID: '))
        cur = con.cursor()
        #cur.execute(f'SELECT * FROM employee WHERE id = {id}')
        cur.execute('SELECT * FROM employee')
        employees = cur.fetchall()

        from_db = []
        for employee in employees:
            result = list(employee)
            from_db.append(result)
        columns = ["Id", "Name", "Salary", "Id_Dep", "Id_Sup"]
        df = pd.DataFrame(from_db, columns=columns)
        print(df)
    elif option == 2:
        print('\n')
    elif option == 3:
        print('\n')
    elif option == 4:
        print('\n')
    elif option == 5:
        print('\n')
    elif option == 6:
        print('\n')
    elif option == 7:
        print('\n')
    elif option == 8:
        print('\n')
    elif option == 9:
        print('\n')
    elif option == 10:
        print('\n')
    elif option == 100:
        print('\n')
    else:
        print("Invalid Option")

    print("\n")
    menu()
    option = int(input("Insert the command that you want to execute:"))

print("Thanks for using this program. See you soon")