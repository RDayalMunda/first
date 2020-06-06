import sqlite3
Library=sqlite3.connect('Library.db')
curbook=Library.cursor()

#creating table
curbook.execute('''CREATE TABLE books (
BookID INTEGER PRIMARY KEY,
title TEXT (40) NOT NULL,
authors TEXT (40),
price REAL);''')

#inserting records in  the book table
curbook.execute("INSERT INTO books (BookID, title, authors, price) VALUES(1, 'Python Crash Cource', 'Eric Matthews', 270.50);")
curbook.execute("INSERT INTO books (BookID, title, authors, price) VALUES(2, 'Think Python', 'Allan B. Drowney', 475);")
curbook.execute("INSERT INTO books (BookID, title, authors, price) VALUES(3, 'Head-First Python', 'Paul Barry', 670.50);")
curbook.execute("INSERT INTO books (BookID, title, authors, price) VALUES(4, 'Learn Python the Hard Way', 'Zed A. Shaw', 910.50);")
curbook.execute("INSERT INTO books (BookID, title, authors, price) VALUES(5, 'Python Programming', 'John Zelle', 862.50);")
curbook.execute("INSERT INTO books (BookID, title, authors, price) VALUES(6, 'A Byte of Python', 'C.H. Swaroop', 741.50);")
curbook.execute("COMMIT;")

Library.close()
