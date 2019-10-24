start = int(input("Start:"))
end = int(input("End:"))

from PyPDF2 import PdfFileWriter, PdfFileReader

with open("2004 - Code Complete 2 - MS Press.pdf", "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()

    numPages = input1.getNumPages()
    print("document has %s pages." % numPages)

    for i in range(start-1, end):
        page = input1.getPage(i)
        print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        page.trimBox.lowerLeft = (160, 110)
        page.trimBox.upperRight = (505, 720)
        page.cropBox.lowerLeft = (160, 110)
        page.cropBox.upperRight = (505, 720)
        output.addPage(page)

    with open("../Desktop/out.pdf", "wb") as out_f:
        output.write(out_f)
    
print("Done")