import json
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
Table Name: mn_jhn_1 (book_name:str | chapter:int | verse_number:int | verse_text:text)
"""

with open("en_jhn_1.json") as jsonfile:
	db=json.load(jsonfile)
	book_name=db["book"]["bookCode"]
	chapter=db["chapters"]
	# print(chapter)
	# en_jhn = "create table en_jhn (id bigint, book_name varchar(128), chapter varchar(256), verse_number varchar(256), verse_text text);"
	# cursor.execute(en_jhn)
	# conn.commit()
	for i in chapter:
		chapterNumber= i["chapterNumber"]
		# print(chapterNumber)
		contents=i["contents"]
		# print(contents)
		for j in contents:
			verse_number=j["verseNumber"]
			# print(verse_number)
			versetext=j["verseText"]
			# print(versetext)
			add_data =""" INSERT into en_jhn (id, book_name, chapter, verse_number, verse_text) VALUES
			(%s, %s, %s, %s, %s)"""
			mycursor.execute(add_data,(verse_number, book_name, chapterNumber, verse_number, versetext))
			mydb.commit()
			count = mycursor.rowcount
			print(count, "Record inserted successfully into en_jhn table")
#en_jhn=mycursor.fetchall()
#print(en_jhn)
#mydb.commit()

#en_jhn = "CREATE TABLE en_jhn(id bigint,book_name Varchar(128),chapter varchar(256),verse_number varchar(260),verse_text text)"
#mycursor.execute(en_jhn)
#mydb.commit()














