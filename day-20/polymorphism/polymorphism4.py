# ploymorphism using common function
class Pdf:
    def open(self):
        print("Opening PDF")


class Word:
    def open(self):
        print("Opening Word")


class Excel:
    def open(self):
        print("Opening Excel")

def open_file(obj):
    obj.open()

pdf = Pdf()
word = Word()
excel = Excel()
open_file(pdf)
open_file(word)
open_file(excel)