from django.shortcuts import render, redirect
from .models import Library , Book, Author
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.utils.decorators import method_decorator


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {"books":books}
    return render( request, 'relationship_app/list_books.html', context) 

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

def register(request):
    form = UserCreationForm()
    return render(request, 'relationship_app/register.html',{'form':form})

permission_required("relationship_app.can_add_book")
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        author_obj = Author.objects.create(name=author)
        Book.objects.create(title=title,author=author_obj)
        return redirect("books")
    return render(request, "relationship_app/add_book.html")

@permission_required("relationship_app.can_change_book")
def edit_book(request, book_id):
    book = Book.objects.get(book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("books")

    return render(request, "relationship_app/edit_book.html", {"book": book})
@permission_required("relationship_app.can_delete_book")
def delete_book(request, book_id):
    book = Book.objects.get(book_id)
    if request.method == "POST":
        book.delete()
        return redirect("books")

    return render(request, "relationship_app/delete_book.html", {"book": book})


def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


# --- Admin View ---
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

# --- Librarian View ---
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")