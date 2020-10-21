from tkinter import Tk, Menu, Scrollbar, Text, N, E, W, S, RIGHT, Y, END
import os
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

class Note_book:
    def __init__(self):
        self.__root = Tk()
        self.__root.title('Untitled - Text Editor')
        self.__root.geometry('640x320')
        ##ICON
        try:
            self.__root.wm_iconbitmap("note.ico")
        except:
            print("'note.ico' was not found in root directory.")
        
        self.__textArea = Text(self.__root, undo = True)

        self.__edited = False
        self.__filename = None
        
        self.__menubar = Menu(self.__root)
        self.__root.config(menu=self.__menubar)

        ###FILE MENU
        self.__fileMenu = Menu(self.__root, tearoff = 0)
        self.__fileMenu.add_command(label='New', command=self.__new)
        self.__fileMenu.add_command(label='Open', command=self.__open)
        self.__fileMenu.add_separator()
        self.__fileMenu.add_command(label='Save', command=self.__save)
        self.__fileMenu.add_command(label='Save as', command=self.__saveas)
        self.__fileMenu.add_separator()
        self.__fileMenu.add_command(label='Exit', command=self.__exit)
        ##FILE submenu options
        self.__menubar.add_cascade(label='File', menu=self.__fileMenu)

        ###EDIT MENU
        self.__editMenu = Menu(self.__menubar, tearoff = 0)
        ##EDIT submenu options
        self.__editMenu.add_command(label='Undo', command=self.__textArea.edit_undo)
        self.__editMenu.add_command(label='Redo', command=self.__textArea.edit_redo)
        self.__editMenu.add_separator()
        self.__editMenu.add_command(label="Cut", command=self.__cut)
        self.__editMenu.add_command(label="Copy", command=self.__copy)
        self.__editMenu.add_command(label="Paste", command=self.__paste)
        self.__menubar.add_cascade(label='Edit', menu=self.__editMenu)
        

 
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        self.__textArea.grid(sticky = N+E+S+W)
        self.__scrollbar = Scrollbar(self.__textArea)    
        
        ##scrollbar auto adjusting
        self.__scrollbar.pack(side=RIGHT, fill=Y)
        self.__scrollbar.config(command=self.__textArea.yview)
        self.__textArea.config(yscrollcommand=self.__scrollbar.set)
        

        ####menu shortcuts
        self.__root.bind('<Control-n>', lambda event: self.__new())
        self.__root.bind('<Control-o>', lambda event: self.__open())
        self.__root.bind('<Control-s>', lambda event: self.__save())
        self.__root.bind('<Control-Shift-s>', lambda event: self.__saveas())

        
        self.__root.mainloop()

    ##edit menu methods
    def __cut(self):
        print('cutting')
        print('self.__menubar= ', self.__menubar)
        print('self.__editmenu= ', self.__editmenu)
        self.__textArea.event_generate("<<Cut>>")

    def __copy(self):
        print('copying')
        self.__textArea.event_generate("<<Copy>>")

    def __paste(self):
        print('pasting')
        self.__textArea.event_generate("<<Paste>>")


##file menu methods
    ##NEW FILE
    def __new(self):
        print(self.__filename)
        self.__filename = None
        self.__root.title('Untitled - Text Editor')
        self.__textArea.delete(1.0, END)
        print('newed')

    ##OPEN EXISTING FILE
    def __open(self):
        self.__filename =askopenfilename(defaultextension='.txt',
                                         filetypes=[('All Files', '*.*'),
                                                    ('Text Documents', '*.txt*')])
        if self.__filename == '':
            self.__filename = None
        else:
            self.__root.title(os.path.basename(self.__filename) + " -Text Editor")
            self.__textArea.delete(1.0, END)
            file=open(self.__filename, "r")
            self.__textArea.insert(1.0, file.read())
            file.close()

    ###SAVE NEW FILE OR OVERWRITE IT
    def __save(self):
        if self.__filename == None:
            self.__saveas()
        else:
            text = self.__textArea.get('1.0','end-1c')
            file = open(self.__filename, 'w')
            file.write(text)
            file.close()
            print('saved')

    def __saveas(self):
        self.__filename = asksaveasfilename(initialfile='Untitled.txt',
                                          defaultextension='.txt',
                                          filetypes=[('Text Documents','*.txt*'),
                                                     ('All Files', '*.*')])
        if self.__filename == '':
            self.__filename = None
        else:
            file = open(self.__filename, 'w')
            file.write(self.__textArea.get(1.0, END))
            file.close
            self.__root.title(os.path.basename(self.__filename) + " -Text Editor")
            print('saved as')

    def __exit(self):
        print('exitted')
        self.__root.destroy()

    ###file menu methods

n1= Note_book()
