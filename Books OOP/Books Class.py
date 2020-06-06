#Python_M4Assignment
class Book:
    def __init__(self, a='unspecified_title', b="unspecified_author", c='unspecified_publisher', d=0, e=0, f=0):
        self._title=a
        self._author=b
        self._publisher=c
        self._price=d
        self._royalty=e
        self._sold=f
    def ShowInfo(self):
        print('Title:  ', self._title)
        print('Author:  ', self._author)
        print('Publisher: ', self._publisher)
        print('Price:  ₹', self._price)
        print('Royalty:  ₹', self._royalty)
        print('Sold: ', self._sold)

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_publisher(self):
        return self._publisher

    def get_price(self):
        return self._price

    def get_royalty(self):
        return self._royalty

    def get_sold(self):
        return self._sold

    def set_title(self, a):
        self._title=a
        return
    
    def set_author(self, a):
        self._author=a
        return

    def set_publisher(self, a):
        self._publisher=a
        return

    def set_price(self, a):
        if type(a)==str:
            print("Price cant' be a string.")
        elif a<0 :
            print("Price can't be -ve.")
        else:
            self._price=a
            self.royalty()
        return

    def set_sold(self, a):
        if type(a)==str:
            print("Copies sold can't be a string.")
        elif a<0:
            print("Copies sold can't be -ve.")
        else:
            self._sold=a
            self.royalty()
        return

    def royalty(self):
        if self._sold <= 500:
            self._royalty = self._sold*(self._price*0.1)
            
        elif self._sold > 500 and self._sold<= 1500:
            self._royalty = 500*(self._price*0.1)
            self._royalty = self._royalty + (self._sold-500)*(self._price*0.125)
            
        else:
            self._royalty = 500*(self._price*0.1)
            self._royalty = self._royalty + 1000*(self._price*0.125)
            self._royalty = self._royalty + (self._sold-1500)*(self._price*0.15)
        print('Royalty for %s is ₹%d'%(self._title, self._royalty))

#ebook child class
class Ebook(Book):
    def __init__(self, a='unspecified_title', b="unspecified_author", c='unspecified_publisher', d=0, e=0, f=0, g='unspecified_format'):
        super().__init__(a,b,c,d,e,f)
        self._format=g
        self._gst = 12

    def set_format(self, a):
        self._format = a

    def get_format(self):
        return self._format

    def royalty(self):
        if self._sold <= 500:
            self._royalty = self._sold*(self._price*0.1)
            
        elif self._sold > 500 and self._sold<= 1500:
            self._royalty = 500*(self._price*0.1)
            self._royalty = self._royalty + (self._sold-500)*(self._price*0.125)
            
        else:
            self._royalty = 500*(self._price*0.1)
            self._royalty = self._royalty + 1000*(self._price*0.125)
            self._royalty = self._royalty + (self._sold-1500)*(self._price*0.15)
        self._royalty = self._royalty-(self._royalty*0.12)
        print('Royalty for %s is ₹%d'%(self._title, self._royalty))
        







