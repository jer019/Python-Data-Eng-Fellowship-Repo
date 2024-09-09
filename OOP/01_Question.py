# Write a Java class Book with following features:
# 	Private Instance variables :
# 	title for the title of book of type String.
# 	author for the author’s name of type String.
# 	price for the book price of type double.
# 	Constructor:
# 	__init__ (Book title, Author name, book  price): A constructor with parameters, it creates the Author object by setting the the fields to the passed values. Note that values should be assigned via the setter methods created for each varible
# 	Instance methods:
# 	setTitle(String title): Used to set the title of book.
# 	setAuthor(String author): Used to set the name of author of book.
# 	setPrice(double price): Used to set the price of book.
# 	getTitle(): This method returns the title of book.
# 	getAuthor(): This method returns the author’s name of book.
# 	toString(): This method printed out book’s details to the screen
# Create 3 objects of book class and display the information of the books.


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def set_title(self, title):
        self.title = title
    def set_author(self, author):
        self.author = author
    def set_price(self, price):
        self.price = price
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}"
novel1 = Book("Umrao Jaan Ada", "Mirza Hadi Ruswa", 500)
novel2 = Book("Bano", "Razia Butt", 700)
novel3 = Book("Manto Ke Afsanay", "Saadat Hasan Manto", 1500)
print("Urdu Novel 1 Information:")
print(novel1)
print("\nUrdu Novel 2 Information:")
print(novel2)
print("\nUrdu Novel 3 Information:")
print(novel3)

