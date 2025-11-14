# query_samples.py

import django
import os

# --- Setup Django environment manually so this script can run independently ---
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# -----------------------------
# 1️⃣ Query all books by a specific author
# -----------------------------
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"\nBooks by {author.name}:")
        for book in books:
            print(f" - {book.title}")
    except Author.DoesNotExist:
        print(f"\nNo author found with name '{author_name}'.")


# -----------------------------
# 2️⃣ List all books in a library
# -----------------------------
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library.name} Library:")
        for book in books:
            print(f" - {book.title}")
    except Library.DoesNotExist:
        print(f"\nNo library found with name '{library_name}'.")


# -----------------------------
# 3️⃣ Retrieve the librarian for a library
# -----------------------------
def get_librarian_for_library(librarian_name):
    try:
        library = Librarian.objects.get(library=librarian_name)
        librarian = library.librarian  # via OneToOneField relationship
        print(f"\nLibrarian for {library.name} Library: {librarian.name}")
    except Library.DoesNotExist:
        print(f"\nNo library found with name '{librarian_name}'.")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian assigned to '{librarian_name}'.")


# -----------------------------
# Example usage (for testing)
# -----------------------------
if __name__ == "__main__":
    # Replace these names with actual objects in your database
    get_books_by_author("Chinua Achebe")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
