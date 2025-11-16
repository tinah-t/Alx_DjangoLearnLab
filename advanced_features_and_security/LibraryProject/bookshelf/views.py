
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Article
from django import forms
from .models import Book
from .forms import SearchForm, BookForm
from .forms import ExampleForm

# Anyone with 'can_view' permission
@permission_required('bookshelf.can_view', raise_exception=True)
def list_articles(request):
    articles = Article.objects.all()
    return render(request, "bookshelf/list_articles.html", {"articles": articles})

# Only users with 'can_create'
@permission_required('bookshelf.can_create', raise_exception=True)
def create_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article.objects.create(
            title=title,
            content=content,
            created_by=request.user
        )
        return render(request, "bookshelf/article_created.html", {"article": article})
    return render(request, "bookshelf/create_article.html")

# Only users with 'can_edit'
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.title = request.POST["title"]
        article.content = request.POST["content"]
        article.save()
        return render(request, "bookshelf/article_updated.html", {"article": article})
    return render(request, "bookshelf/edit_article.html", {"article": article})

# Only users with 'can_delete'
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return render(request, "bookshelf/article_deleted.html")
def book_list(request):
    """
    Display a list of books (or articles) in the system.
    """
    books = Article.objects.all()   # or Book.objects.all()
    context = {"books": books}
    return render(request, "bookshelf/book_list.html", context)

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

def search_books(request):
    form = SearchForm(request.GET)

    books = []

    # FORM VALIDATION PREVENTS MALICIOUS INPUT
    if form.is_valid():
        query = form.cleaned_data["query"]
        books = Book.objects.filter(title__icontains=query)

    return render(request, "bookshelf/search_results.html", {
        "form": form,
        "books": books
    })

def search_books(request):
    form = SearchForm(request.GET)
    books = []

    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)

    return render(request, "books/search_results.html", {
        "form": form,
        "books": books
    })
