books = ["Python", "Java", "C++"]

book = input("Enter new book: ")
books.append(book)

book = input("Enter book to search: ")
if book in books:
    print("Book found")
else:
    print("Book not found")

book = input("Enter book to remove: ")
if book in books:
    books.remove(book)

print("Books:", books)
print("Total books:", len(books))
