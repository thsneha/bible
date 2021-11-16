import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123@123",
    database="python_db"
)
print(mydb)
print(mydb)
if(mydb):
    print("connection successfully ")
else:
    print("no connection established")
mycursor=mydb.cursor()

"""
Table Name: ml_jhn (book_name:str | chapter:int | verse_number:int | verse_text:text)
"""
with open("ml_jhn_1.txt", mode="r", encoding="utf-8") as file:
  data = file.read()

  file_name = file.name.split(".")[0] #to remove .txt part from file name
  file_name_data = file_name.split("_") #For printing this way [ml][jhn1][1]
  print(file_name_data)
  table_name = file_name_data[0] + "_" + file_name_data[1] #print ml_jhn
  book_name = file_name_data[1]     #print jhn
  chapter_number = file_name_data[2] #print 1
  print(table_name, book_name, chapter_number) #print ml_jh

  #ml_jhn = "CREATE TABLE "+table_name+"(id bigint,book_name Varchar(128),chapter varchar(256),verse_number varchar(260),verse_text text)"
  #mycursor.execute(ml_jhn)
  #mydb.commit()

  #t1 = ("SELECT * from ml_jhn_1")
  #mycursor.execute(t1)
  #table = mycursor.fetchall()
  #print(table)
  jhn_data_1=data.split(".")#to split from fullstop
  #print(jhn_data_1)
  for v in jhn_data_1:
      if v[0].isdigit():#check the first sentence is digit is present in it then go ahead.
          verse_number = v[0:2].rstrip()#extracting the number,that means if it is a single digit then printing first digit v[0]and removing spaces
          print(verse_number)#if  it is two digit then v[0][1] and removing spaces.
          verse_text=v[3:] #extract the verse text and printing from v[3]
          print(verse_text)
          add_data = """INSERT INTO ml_jhn (id, book_name, chapter, verse_number, verse_text) VALUES (%s,%s,%s,%s,%s)"""
          mycursor.execute(add_data, (verse_number, book_name, chapter_number, verse_number, verse_text))
          mydb.commit()
          count = mycursor.rowcount
          print(count, "Record inserted successfully into ml_jhn table")
#ml_jhn = mycursor.fetchall()
#print(ml_jhn)
mydb.commit()

#add_data = """ INSERT INTO ml_jhn (id, book_name, chapter, verse_number, verse_text) VALUES (%s,%s,%s,%s,%s)"""





