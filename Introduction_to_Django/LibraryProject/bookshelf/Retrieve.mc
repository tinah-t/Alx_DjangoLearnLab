get_book = Book.objects.get(title="1984")
print(get_book.__dict__) 
# Result ={'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}