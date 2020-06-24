import psycopg2
import pandas as pd
import csv
def create_tabel():
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=jahnavi")
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS mapping(
                place_name text,
                admin_name1 text,
                latitude float,
                longitude float,
                country text ,
                pin integer PRIMARY KEY
                )""")
    conn.commit()
    conn.close()

def insert(place_name , admin_name1 , latitude , longitude , Country , pin):
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=jahnavi")
    cur = conn.cursor() 
    cur.execute("INSERT INTO mapping(place_name , admin_name1 , latitude , longitude , Country , pin) VALUES(%s,%s,%s,%s,%s,%s);" , (place_name , admin_name1 , latitude , longitude , Country , pin))   
    conn.commit()
    conn.close()

create_tabel()
data = pd.read_csv("D:\\pincode-master\\data\\IN.csv") 
pincode = data["key"].str.split("/", n = 1, expand = True) 
data["Country"]= pincode[0] 
data["pin"]= pincode[1]
data.drop(columns =["key"], inplace = True) 
data.drop(columns =["accuracy"], inplace = True)

df = pd.DataFrame(data)  
df.to_csv("D:\\pincode-master\\data\\OUT.csv ", index=False)
  

with open("D:\\pincode-master\\data\\OUT.csv ", 'r') as f:
    reader = csv.reader(f)
    columns = next(reader)
    f.seek(0)

    for row in f:
        my_row = next(reader)
        place_name = "'"+my_row[0]+"'"
        admin_name1 = "'"+my_row[1]+"'"
        latitude = my_row[2]
        longitude = my_row[3]
        Country = "'"+my_row[4]+"'"
        pin = my_row[5]
        insert(place_name , admin_name1 , latitude , longitude , Country , pin)

       