delete_book = Book.objects.get(author="George Orwell")
delete_book.delete()

# the book will be deleted
