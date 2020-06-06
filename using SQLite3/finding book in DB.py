import sqlite3

def lib():
    Library=sqlite3.connect('Library.db')
    curbook=Library.cursor()

    nam=input('\nEnter Book Title:\t')
    sel="SELECT * FROM books where title ='"+nam+"';"
    curbook.execute(sel)
    record=curbook.fetchone()
    if record == None:
        print('No books with that names exist yet!\n')
    else:
        print('%d\t%s\t%s\t₹%d'%(record[0], record[1], record[2], record[3]))
        copy=int(input('\nNo. of copies: '))

        while True:
            choice=input('Add more books? Y/N\t')
            if choice.upper() == 'Y':
                copy = copy + int(input('Books to add:\t')) 
            elif choice.upper() == 'N':
                break
            else:
                print('Wrong Key!')
        print('\nTotal Cost = ₹%d\n\n'%(copy*record[3]))
    Library.close()
    choice=input('Transations: Search books: (Y/N)\t')
    if choice.upper()=='Y':
        lib()
    elif choice.upper()=='N':
        print('Exited')
        Library.close()
  
lib()



