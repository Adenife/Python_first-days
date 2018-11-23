import sqlite3

sqlite_file = 'C:/Users/OLUWANIFEMI ADEOLA/Pictures/sqlite/sqlitestudio-3.1.1/SQLiteStudio/DB/db1.db'
db = sqlite3.connect(sqlite_file)

cursor = db.cursor()

name = 'Adeoye Tayo Jeremiah'
num = '5557241'

cursor.execute
cursor.execute("INSERT INTO user(Name, Reg) VALUES(?,?)", (name, num))
print('First user inserted')
db.commit()

cursor.execute('''SELECT * FROM user''')
user = cursor.fetchone()
print(user)
db.close()
