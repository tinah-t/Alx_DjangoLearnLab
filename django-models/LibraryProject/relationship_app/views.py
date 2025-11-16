from django.shortcuts import render, get_object_or_404, redirect
from .models import Library , Book, Author
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required
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
