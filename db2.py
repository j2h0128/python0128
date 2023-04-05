#db1.py

import sqlite3

#연결객체 생성(임시로 메모리에 저장)
con = sqlite3.connect(":memory:")

#실제 파일에 저장히기
#con=sqlite3.connect("c:\\work\\sample.db")
cur = con.cursor()

#SQL구문을 실행할 커서 객체 리턴
cur.execute("create table if not exists PhoneBook "
        + "(id integer primary key autoincrement, "
        + "name text, phoneNum text);") 

#1건 입력 
cur.execute("insert into PhoneBook (name, phoneNum) values "
    + "('홍길동','010-111-1234');")

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

#외부에서 파라메터로 입력 받기
name = "이순신" 
phoneNumber = "010-222-1234" 
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);",
(name, phoneNumber)) 

#다중의 행을 입력(2차원 배열)
datalist=(("전우치", "010-1233-2345"),("박문수", "070-5443-7655"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);",
datalist) 



#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print("{0}, {1}, {2}".format(row[0], row[1], row[2]))

# #결과를 확인
cur.execute("select * from PhoneBook;")
print("------fetchone()-----------")
print(cur.fetchone())
print("------fetchmany(2)-----------")
print(cur.fetchmany(2))
print("------fetchall()-----------")
print(cur.fetchall())
print("------fetchall()-----------")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())


#정상적으로 완료
con.commit()