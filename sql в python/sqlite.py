import sqlite3 as sq

#упр 1 - Вывести список книг
with sq.connect(r'C:\Users\79252\OneDrive\Рабочий стол\test.db') as con:
    cur = con.cursor()
    cur.execute(""" SELECT title FROM books
    """)
    result = cur.fetchall()
    print('список книг',result)
#
# упр 2 - Вывести список читателей
with sq.connect(r'C:\Users\79252\OneDrive\Рабочий стол\test.db') as con:
    cur = con.cursor()
    cur.execute(""" SELECT name FROM readers
    """)
    result = cur.fetchall()
    print('список читателей ',result)

# упр 3 - добавить книгу
with sq.connect(r'C:\Users\79252\OneDrive\Рабочий стол\test.db') as con:
    cur = con.cursor()
    cur.execute('''INSERT INTO books (author,title,publish_year,id)
    VALUES ('Булгаков','Собачье сердце','1987','7');''')
    con.commit()

# # для проверки
# with sq.connect(r'C:\Users\79252\OneDrive\Рабочий стол\test.db') as con:
#     cur = con.cursor()
#     cur.execute(""" SELECT title FROM books
#     """)
#     result = cur.fetchall()
#     print('список книг',result)

# упр 4 - Добавить читателя
with sq.connect(r'C:\Users\79252\OneDrive\Рабочий стол\test.db') as con:
    cur = con.cursor()
    cur.execute('''INSERT INTO readers (id,name) VALUES ('6','Sergey');''')
    con.commit()

#  # для проверки
# with sq.connect(r'C:\Users\79252\OneDrive\Рабочий стол\test.db') as con:
#     cur = con.cursor()
#     cur.execute(""" SELECT name FROM readers
#     """)
#     result = cur.fetchall()
#     print('список читателей ',result)


# упр 5 - выдать книгу читателю
with sq.connect(r'C:\Users\79252\OneDrive\Рабочий стол\test.db') as con:
    cur = con.cursor()
    cur.execute('''INSERT INTO records (readers_id, book_id,taking_date,returning_date)
     VALUES ('2','1','2023-03-05','NULL');''')
    con.commit()

# упр 6 - принять книгу
with sq.connect(r'C:\Users\79252\OneDrive\Рабочий стол\test.db') as con:
    cur = con.cursor()
    cur.execute('''UPDATE records
    SET returning_date = '2023-05-04'
    WHERE taking_date = '2023-05-03' ''')
    con.commit()

# #для проверки
# with sq.connect(r'C:\Users\79252\OneDrive\Рабочий стол\test.db') as con:
#     cur = con.cursor()
#     cur.execute(""" SELECT taking_date FROM records
#     """)
#     result = cur.fetchall()
#     print('список книг',result)