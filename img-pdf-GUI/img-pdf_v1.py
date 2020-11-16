from tkinter import Tk, Listbox, Grid, Scrollbar, Button, END, SINGLE, W,E,N,S, HORIZONTAL
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PyPDF2 import PdfFileMerger
from PIL import Image
from os import remove

class Pdf_converter:
    def __init__(self):
        self._root = Tk()
        self._root.geometry("500x400")
        self._root.title("IMGPDF")
        self._Elements()
        Grid.rowconfigure(self._root, 0, weight=1)
        Grid.columnconfigure(self._root, 0, weight=1)
        self.supportedfiles=[('PDF files', '*.pdf*'),
                             ('jpg files', '*.jpg*'),
                             ('png files', '*.png*'),
                             ('gif files', '*.gif*'),
                             ('All files', '*.*')]
        self.openfiles = []
        self._root.mainloop()
    def _Elements(self):
        ##create button
        self._create = Button(self._root, text="Create", command=self._Create_pdf)

        ##lift up
        self._lift = Button(self._root, text="↑ Lift Up", command=self._Lift_up)
        
        ##push down
        self._push = Button(self._root, text="↓ Push Down", command=self._Push_down)
        
        ##addfiles
        self._addfiles = Button(self._root, text="Add Files", command=self._Select_files)

        ##scrollbars
        self._hscroll = Scrollbar(self._root, orient=HORIZONTAL)
        self._vscroll = Scrollbar(self._root)
        ##Listwidget / List box
        self._listbox = Listbox(self._root, width=40,
                                xscrollcommand=self._hscroll.set,
                                yscrollcommand=self._vscroll.set)
        self._hscroll.config(command=self._listbox.xview)
        self._vscroll.config(command=self._listbox.yview)

        #packing
        self._listbox.grid(column=0, columnspan=4, row=0, rowspan=6, sticky=N+E+W+S)
        self._hscroll.grid(column=0, row=6, columnspan=4, sticky=W+E)
        self._vscroll.grid(column=4, row=0, rowspan=6, sticky=N+S)
        self._addfiles.grid(column=3, row=7, sticky=W+E)
        self._create.grid(column=2, row=7, sticky=W+E)
        self._push.grid(column=5, row=1, sticky=S+E+W)
        self._lift.grid(column=5, row=0, sticky=N+W+E)
        

        
    def _Lift_up(self):
        #"to lift the element up."
        try:
            current = self._listbox.curselection()[0]
            value = self._listbox.get(current)
            if current != 0:
                upper = current-1
                self._listbox.insert(current, self._listbox.get(upper))
                self._listbox.delete(current+1)

                self._listbox.insert(upper, value)
                self._listbox.delete(upper+1)
                self._listbox.selection_set(upper)
                self._listbox.activate(upper)
        except:
            print("Error in Lift Up")
    def _Push_down(self):
        #"to push the item down."
        try:
            current = self._listbox.curselection()[0]
            value = self._listbox.get(current)
            if current < self._listbox.size()-1:
                lower = current+1
                self._listbox.insert(current, self._listbox.get(lower))
                self._listbox.delete(current+1)

                self._listbox.insert(lower, value)
                self._listbox.delete(lower+1)
                self._listbox.selection_set(lower)
                self._listbox.activate(lower)
        except:
            print("Error in Push Down")
    def _Select_files(self):
        names = askopenfilename(defaultextension=".pdf",
                            filetypes=self.supportedfiles,
                            multiple=True)
        for file in names:
            self._listbox.insert(END, file)

    def _Create_pdf(self):
        #"To create pdf of the images and join then in the given sequence."
        self.final=asksaveasfilename(initialfile="merged.pdf",
                            defaultextension=".pdf",
                            filetypes=[('PDF files','*.pdf*')])
        self._merger()
            
    def _merger(self):
        file_list = self._listbox.get(0, END)
        newfile = self.final[:-4]+'0.pdf'
        if file_list[0][-4:]=='.jpg' or file_list[0][-4:]=='.png' or file_list[0][-4:]=='.gif':
            fname = file_list[0][:-4]+'.pdf'
            image = Image.open(file_list[0])
            pdf = image.convert('RGB')
            pdf.save(newfile)
            image.close()
        elif file_list[0][-4:]=='.pdf':
            pdf = open(file_list[0], 'rb')
            image = pdf.read()
            pdf.close()
            pdf = open(newfile, 'wb')
            pdf.write(image)
            pdf.close()

        for i in range(len(file_list)):
            if i!=0:
                pdfname = self.final[:-4]+'_'+str(i)+'.pdf'
                if file_list[i][-4:]=='.jpg' or file_list[i][-4:]=='.png' or file_list[i][-4:]=='.gif':
                    fname = file_list[i][:-4]+'.pdf'
                    image = Image.open(file_list[i])
                    pdf = image.convert('RGB')
                    pdf.save(pdfname)
                    image.close()
                elif file_list[i][-4:]=='.pdf':
                    pdf = open(file_list[i], 'rb')
                    image = pdf.read()
                    pdf.close()
                    pdf = open(pdfname, 'wb')
                    pdf.write(image)
                    pdf.close()

                pdflist=[newfile, pdfname]
                merger = PdfFileMerger()
                for pdfs in pdflist:
                    pdf = (open(pdfs, 'rb'))
                    self.openfiles.append(pdf)
                    merger.append(self.openfiles[-1])

                newfile = newfile = self.final[:-4]+str(i)+'.pdf'
                with open(newfile, 'wb') as f:
                    merger.write(f)

                self.openfiles[-1].close()
                self.openfiles[-2].close()

                remove(pdfname)
                remove(self.final[:-4]+str(i-1)+'.pdf')

        pdf = open(newfile, 'rb')
        data = pdf.read()
        pdf.close()
        remove(newfile)
        pdf = open(self.final, 'wb')
        pdf.write(data)
        pdf.close()
                        
pdf=Pdf_converter()
