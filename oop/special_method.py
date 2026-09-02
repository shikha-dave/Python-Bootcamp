mylist = [1, 2, 3]
len(mylist)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
print(len(my_book))  # Uses the __len__ method
print(str(my_book))  # Uses the __str__ method
print(repr(my_book))  # Uses the __repr__ method