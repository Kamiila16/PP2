class MyClass:
    def getString(self):
        self.word=input()
    def printString(self):
        print(self.word.upper())
res=MyClass()
res.getString()
res.printString()