

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author,price):
        super().__init__(title, author)
        self.price = price
    def display(self):
        print('Title:',title)
        print('Author:',author)
        print('Price:',self.price)
        pass

