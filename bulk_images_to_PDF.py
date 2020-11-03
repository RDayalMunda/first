from os import walk, getcwd, remove, system
system('cls')
from PyPDF2 import PdfFileMerger
from PIL import Image
system('title ' +'Bulk_images_to_PDF_creator')


f = []
for (dirpath, dirnames, filenames) in walk(getcwd()):
    f.extend(filenames)
    break
ilist =[]
for names in f:
    if names[-3:] =='jpg' or names[-3:] == 'png':
        ilist.append(names)

fname = ilist[0][:-3] + 'pdf'
img = Image.open(ilist[0])
iml = img.convert('RGB')
iml.save('newfile_0.pdf')
img.close()
newfile = 'newfile_0.pdf'

base = fname
openfile =[]
for i in range(len(ilist)):
    if i== 0:
        print('completed: 0.00 %')
        print('Do not delete any pdf or image files in this directory!')
        pass
    else:
        pdfname = 'pdf_'+str(i)+'.pdf'
        image = Image.open(ilist[i])
        pdf = image.convert('RGB')
        pdf.save(pdfname)
        image.close()

        pdflist=[newfile, pdfname]
        merger = PdfFileMerger()
        for pdfs in pdflist:
            pdf = (open(pdfs, 'rb'))
            openfile.append(pdf)
            merger.append(openfile[-1])

        newfile = 'newfile_'+str(i)+'.pdf'
        with open(newfile, 'wb') as f:
            merger.write(f)
        ###to close the open files so extra files could be deleted
        openfile[-1].close()
        openfile[-2].close()
        sleep(2)
        remove(pdfname)
        prevfile = 'newfile_'+str(i-1)+'.pdf'
        remove(prevfile)
        system('cls')
        print('completed: %.2f'%(i/len(ilist)*100), '%')
        print('Do not delete any pdf or image files in this directory!')
system('cls')
input('COMPLETED\nfile name = %s'%(newfile))
