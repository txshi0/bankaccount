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
        self.books.append(member)

        print(f"="*30)
        print("Member added successfully")
        for b in self.members:
            print(b)
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
        pass

    if choice == "4":
        pass

    if choice == "5":
        pass

    if choice == "6":
        pass