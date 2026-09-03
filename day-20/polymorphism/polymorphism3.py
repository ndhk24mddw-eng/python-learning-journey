class Pdf:
    def open(self):
        print('open the pdf file :')
class Word:
    def open(self):
        print('open the word file :')
class Excel:
    def open(self):
        print('open the excel file :')

objects = [Pdf(),Word(),Excel()]
for obj in objects:
    obj.open()