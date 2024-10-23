import sqlite3

con = sqlite3.connect(r"c:\work\sample.db")

cur = con.cursor()

cur.execute("create table if not exists PhoneBook (Name text, PhoneNum text);")

name ="홍길동"
phoneNumber = "010-111-2222"

datalist = (("전우치", "010-333-4444"), ("박문수", "010-333-5555"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row[0], row[1])

print(cur.fetchall())

con.commit()




