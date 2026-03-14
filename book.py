class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author 
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"Title: {self.title} -- Author: {self.author} -- ISBN: {self.isbn}"

    #Member Class
class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.books_held = []

    def __str__(self):
        return f"Name: {self.name} -- Age: {self.age}"
    
    #Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

        print(f"="*30)
        print("Book added successfully")
        for b in self.books:
            print(b)
        print(f"="*30)

    def add_member(self, member):
        self.members.append(member)

        print(f"="*30)
        print("Member added successfully")
        for b in self.members:
            print(b)
        print(f"="*30)

    def find_book(self, title):
        print(f"="*30)
        for book in self.books:
            if book.title.lower() == title.lower():
                print("Book Found.")
                print(book)
                print(f"="*30)
                return
        print("Book not found.")
        print(f"="*30)

    def find_member(self, name):
        print(f"="*30)
        for member in self.members:
            if member.name.lower() == name.lower():
                print("Member Found.")
                print(member)
                print(f"="*30)
                return
        print("Member is not found.")
        print(f"="*30)

library = Library()

while True:
    print('''=== Library System ===
    Choose Menu
====================
1. ADD BOOK
2. ADD MEMBER
3. FIND BOOK
4. FIND MEMBER
5. BORROW BOOK
6. RETURN BOOK
====================         
''')
    choice = input("Input choice: ")

    if choice == "1":
        title = input("Book Title: ")
        author = input("Author Name: ")
        isbn = input("ISBN Code: ")
        new_book = Book(title=title, author=author, isbn=isbn)
        library.add_book(new_book)

    if choice == "2":
        name = input("Member Name: ")
        age = input("Member Age: ")
        new_member = Member(name=name, age=age)
        library.add_member(new_member)

    if choice == "3":
        title = input("Enter the book title to find: ")
        library.find_book(title)

    if choice == "4":
        name = input("Enter member name to find: ")
        library.find_member(name)

    if choice == "5":
        pass

    if choice == "6":
        pass