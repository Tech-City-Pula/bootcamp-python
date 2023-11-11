# Exercise 1: Define a class Book with two attributes: title and author. Then create an instance of this class and print the title of the book.
# Exercise 2: Add a method to the Book class that prints "[Book title] is written by [author]." Then call this method on your Book instance.

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_info(self):
        print(f"{self.title} is written by {self.author}")
    


# exercise 1

book = Book(author="Matej", title="Book of Ra")
print(book.title)

# exercise 2

book.get_info()