import pandas as pd
import psycopg2
from sqlalchemy import delete

pd.set_option('display.max_columns', None)  # para poder visualizar todas as colunas no display
pd.set_option('display.width', 1000)  # para a largura do display ser de dimensao 1000

races = pd.read_excel('races.xlsx')
races.columns = races.columns.str.replace(' ', '_')  # torna mais facil a utilizaçao das colunas

def menu():
  print("[1] Create connection to the PostgreSQL for Paulo")
  print("[2] Create connection to the PostgreSQL for Miguel")
  print("[3] Create connection to the PostgreSQL for Luis")
  print("[4] Head, Size and Shape of Dataset")
  print("[5] Remove all data from the database")
  print("[6] Add all data to the database")
  print("[0] Let´s work with PostgreSQL and Python.")


menu()
option = int(input("Insert the command that you want to execute:\n"))

while option != 0:
  if option == 1:
    con = psycopg2.connect(
      database="fced_paulo_portela",  # your database is the same as your username
      user="fced_paulo_portela",  # your username
      password="!Pnp2186tenis",  # your password
      host="dbm.fe.up.pt",
      port=5433,  # the database host
      options='-c search_path=public'  # use the schema you want to connect to
    )
    print(con)
  elif option == 2:
    con = psycopg2.connect(
      database="fced_carlos_veloso",  # your database is the same as your username
      user="fced_carlos_veloso",  # your username
      password="tartaruga",  # your password
      host="dbm.fe.up.pt",  # the database host
      port=5433,  # the database host
      options='-c search_path=public'  # use the schema you want to connect to
    )
    print(con)
  elif option == 3:
    con = psycopg2.connect(
      database="username",  # your database is the same as your username
      user="username",  # your username
      password="password",  # your password
      host="dbm.fe.up.pt",  # the database host
      options='-c search_path=schema'  # use the schema you want to connect to
    )
    print(con)
  elif option == 4:
    print(races.head)
    print('\n')
    print('Numero de elementos da matriz')
    print(races.size)
    print('\n')
    print('Dimensão da matriz')
    print(races.shape)
    print('\n')
  elif option == 5:
    cur = con.cursor()
    cur.execute('DELETE FROM sex')
    cur.execute('DELETE FROM nation')
    cur.execute('DELETE FROM runner')
    cur.execute('DELETE FROM age_class')
    cur.execute('DELETE FROM distance')
    cur.execute('DELETE FROM event')
    cur.execute('DELETE FROM classification')
    con.commit()
    print('All data was deleted with success')
  elif option == 6:

    # NATION
    nation = races[['nation']]
    nation_dic = dict()
    lst_nation = list()
    n = 1

    for index, row in nation.iterrows():
      if row['nation'] not in nation_dic.values():
        nation_dic[n] = row['nation']
        key = n
        t = f"INSERT INTO nation VALUES ({key}, '{nation_dic[key]}');"
        lst_nation.append(t)
        n += 1

    for i in range(len(lst_nation)):
      cur = con.cursor()
      cur.execute(lst_nation[i])

    # AGE CLASS
    age_class = races[['age_class']]
    ageclass_dic = dict()
    lst_age_class = list()
    n = 1

    for index, row in age_class.iterrows():
      if row['age_class'] not in ageclass_dic.values():
        ageclass_dic[n] = row['age_class']
        key = n
        t = f"INSERT INTO age_class VALUES ({key}, '{ageclass_dic[key]}');"
        lst_age_class.append(t)
        n += 1

    for i in range(len(lst_age_class)):
      cur = con.cursor()
      cur.execute(lst_age_class[i])

    # DISTANCE
    distance = races[['distance']]
    distance_dic = dict()
    lst_distance = list()
    n = 1

    for index, row in distance.iterrows():
      if row['distance'] not in distance_dic.values():
        distance_dic[n] = row['distance']
        key = n
        t = f"INSERT INTO distance VALUES ({key}, '{distance_dic[key]}');"
        lst_distance.append(t)
        n += 1

    for i in range(len(lst_distance)):
      cur = con.cursor()
      cur.execute(lst_distance[i])

    """ 
    #EVENT
    event = races[['event', 'event_year', 'distance']]
    event_dic = dict()
    lst_event = list()
    n = 1

    for index, row in event.iterrows():
          t = [row['event'], row['event_year'],list(distance_dic.keys())[list(distance_dic.values()).index(row['distance'])]]
          if row['event'] not in event_dic.values():
                event_dic[n] = t
                key = n
                t = f"INSERT INTO event VALUES ({key}, '{event_dic[key][0]}', {int(event_dic[key][1])}, {int(event_dic[key][2])});"
                lst_event.append(t)
                n += 1

    for i in range(len(lst_event)):
          cur = con.cursor()
          cur.execute(lst_event[i])

    """

    con.commit()
    con.close()

    print('All data was inserted with success')
  else:
    print("Invalid Option")

  print("\n")
  menu()
  option = int(input("Insert the command that you want to execute:"))




