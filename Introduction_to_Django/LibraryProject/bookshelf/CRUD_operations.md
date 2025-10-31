new_book = Book(title = "1984", author = "George Orwell", publication_year = "1949")
new_book.save()

# Upon successful creation it will not give us any output.

get_book = Book.objects.get(title="1984")
print(get_book.**dict**)

# Result ={'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}

update_book = Book.objects.get(title="1984")
update_book.title = "Nineteen Eighty-Four"  
update_book.save()

# the title will be updated

delete_book = Book.objects.get(author="George Orwell")
delete_book.delete()

# the book will be deleted
