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
    print("[1] How many runners have more than 50 years old?")
    print("[2] How many runners are in each age class?")
    print("[3] Which runner has more 1st places?")
    print("[4] What are the events with less then 42km distance?")
    print("[5] Plot graphic for ")
    print("---------------------------5 Questions ---------------------------")
    print("[6] Who run the fastest 10K race ever (name, birthdate, time)")
    print("[7] What 10K race had the fastest average time (event, event date)?")
    print("[8] What teams had more than 3 participants in the 2016 maratona (team)?")
    print("[9] What are the 5 runners with more kilometers in total (name, birthdate, kms)?")
    print("[10] What was the best time improvement in two consecutive maratona races (name,birthdate, improvement)?")

    print("[0] Exit the program.")

menu()
option = int(input("Insert the command that you want to execute:\n"))

while option != 0:
    if option == 1:
        cur = con.cursor()
        cur.execute("""""")
        runners = cur.fetchall()
        from_db = []
        for runner in runners:
            result = list(runner)
            from_db.append(result)
        columns = ["Name", "Birth_Date", "Time"]
        df = pd.DataFrame(from_db, columns=columns)
        print(df)
    elif option == 2:
        cur = con.cursor()
        cur.execute("""""")
        runners = cur.fetchall()
        from_db = []
        for runner in runners:
            result = list(runner)
            from_db.append(result)
        columns = ["Name", "Birth_Date", "Time"]
        df = pd.DataFrame(from_db, columns=columns)
        print(df)
    elif option == 3:
        cur = con.cursor()
        cur.execute("""""")
        runners = cur.fetchall()
        from_db = []
        for runner in runners:
            result = list(runner)
            from_db.append(result)
        columns = ["Name", "Birth_Date", "Time"]
        df = pd.DataFrame(from_db, columns=columns)
        print(df)
    elif option == 4:
        cur = con.cursor()
        cur.execute("""""")
        events = cur.fetchall()
        from_db = []
        for event in events:
            result = list(event)
            from_db.append(result)
        columns = ["Name", "Birth_Date", "Time"]
        df = pd.DataFrame(from_db, columns=columns)
        print(df)
    elif option == 5:
        print('\n')
    elif option == 6:
        cur = con.cursor()
        cur.execute("""SELECT name, b_date, MIN(o_time)
FROM classification JOIN event ON event_id = e_id
                    JOIN distance ON event.distance = d_id
                    JOIN runner ON runner_id = r_id
WHERE distance.distance = 10
GROUP BY r_id
HAVING MIN(o_time) <= ALL (SELECT MIN(o_time)
FROM classification JOIN event ON event_id = e_id
                    JOIN distance ON event.distance = d_id
                    JOIN runner ON runner_id = r_id
WHERE distance.distance = 10
GROUP BY r_id)""")
        runners = cur.fetchall()
        from_db = []
        for runner in runners:
            result = list(runner)
            from_db.append(result)
        columns = ["Name", "Birth_Date", "Time"]
        df = pd.DataFrame(from_db, columns=columns)
        print(df)
    elif option == 7:
        cur = con.cursor()
        cur.execute("""SELECT event, e_year
FROM classification JOIN event ON event_id = e_id
                    JOIN distance ON event.distance = d_id
WHERE distance.distance = 10
GROUP BY e_id
HAVING AVG(o_time) <= ALL (SELECT AVG(o_time)
FROM classification JOIN event ON event_id = e_id
                    JOIN distance ON event.distance = d_id
WHERE distance.distance = 10
GROUP BY e_id)""")
        races = cur.fetchall()
        from_db = []
        for race in races:
            result = list(race)
            from_db.append(result)
        columns = ["Event", "Event_Year"]
        df = pd.DataFrame(from_db, columns=columns)
        print(df)
    elif option == 8:
        cur = con.cursor()
        cur.execute("""SELECT team
FROM classification JOIN event ON event_id = e_id
WHERE e_year = 2016 AND event.event = 'maratona' AND team <> 'nan'
GROUP BY team
HAVING COUNT (*) > 3""")
        teams = cur.fetchall()
        from_db = []
        for team in teams:
            result = list(team)
            from_db.append(result)
        columns = ["Team"]
        df = pd.DataFrame(from_db, columns=columns)
        print(df)
    elif option == 9:
        cur = con.cursor()
        cur.execute("""SELECT name, b_date, SUM(distance.distance) AS total_kms
FROM classification JOIN runner ON runner_id = r_id
                    JOIN event ON event_id = e_id
                    JOIN distance on event.distance = d_id
GROUP BY r_id
HAVING SUM(distance.distance) IN (
SELECT SUM(distance.distance)
FROM classification JOIN runner ON runner_id = r_id
                    JOIN event ON event_id = e_id
                    JOIN distance on event.distance = d_id
GROUP BY r_id
ORDER BY SUM(distance.distance) DESC
LIMIT 5
)
ORDER BY SUM(distance.distance) DESC""")
        runners = cur.fetchall()
        from_db = []
        for runner in runners:
            result = list(runner)
            from_db.append(result)
        columns = ["Name", "Birth Date", "Total KM´s"]
        df = pd.DataFrame(from_db, columns=columns)
        print(df)
    elif option == 10:
        cur = con.cursor()
        cur.execute("""SELECT name, b_date, GREATEST(dif_1213, dif_1314, dif_1415, dif_1516) AS improvement
FROM (

SELECT name, b_date, o_time_2012 - o_time_2013 AS dif_1213, o_time_2013 - o_time_2014 AS dif_1314, o_time_2014 - o_time_2015 AS dif_1415, o_time_2015 - o_time_2016 AS dif_1516
FROM (SELECT name, b_date, o_time AS o_time_2012, e_year
      FROM classification JOIN event ON event_id = e_id
                    JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2012) AS year_2012 
FULL OUTER JOIN (SELECT name, b_date, o_time AS o_time_2013, e_year
      FROM classification JOIN event ON event_id = e_id
                          JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2013) AS year_2013 USING(name, b_date)
FULL OUTER JOIN (SELECT name, b_date, o_time AS o_time_2014, e_year
      FROM classification JOIN event ON event_id = e_id
                          JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2014) AS year_2014 USING(name, b_date)
FULL OUTER JOIN (SELECT name, b_date, o_time AS o_time_2015, e_year
      FROM classification JOIN event ON event_id = e_id
                          JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2015) AS year_2015 USING(name, b_date)
FULL OUTER JOIN (SELECT name, b_date, o_time AS o_time_2016, e_year
      FROM classification JOIN event ON event_id = e_id
                          JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2016) AS year_2016 USING(name, b_date)

) AS differences

GROUP BY name, b_date, improvement

HAVING GREATEST(dif_1213, dif_1314, dif_1415, dif_1516) IS NOT NULL

ORDER BY GREATEST(dif_1213, dif_1314, dif_1415, dif_1516) DESC

LIMIT 1
""")
        improvements = cur.fetchall()
        from_db = []
        for improvement in improvements:
            result = list(improvement)
            from_db.append(result)
        columns = ["Name", "Birth Date", "Improvement"]
        df = pd.DataFrame(from_db, columns=columns)
        print(df)
    elif option == 100:
        print('\n')
    else:
        print("Invalid Option")

    print("\n")
    menu()
    option = int(input("Insert the command that you want to execute:"))

print("Thanks for using this program. See you soon")