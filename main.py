import sqlite3
data = sqlite3.connect('mydatabase.db')
sql = data.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS students (id INT, name TEXT, grade TEXT, age INT);')
# sql.execute('INSERT INTO students (id, name, grade, age) VALUES (1872929, "Альб64ерт", "1А", 7);')
#  data.commit()



def get_st(name):
    print(sql.execute('SELECT name, age, grade FROM students WHERE name=?;', (name,)).fetchone())

def update_grade(name, grade):
   print(sql.execute('SELECT * FROM students WHERE name=?;', (name,)).fetchone())
   sql.execute('UPDATE students SET grade=? WHERE name=?;', (grade, name)).fetchone()
   data.commit()
   print(sql.execute('SELECT * FROM students WHERE name=?;', (name,)).fetchone())
# update_grade(name='Альберт', grade='2А')
def del_st(name):
    sql.execute('DELETE FROM students WHERE name=?;', (name,)).fetchone()
    data.commit()
    print(sql.execute('SELECT * FROM students WHERE name=?;', (name,)).fetchone())
del_st(name='Альберт')

# print("Выберите параметр: \n")
# vopr = int(input('Посмотреть - 1\n'
#                 'Перевести в др класс - 2\n '))

