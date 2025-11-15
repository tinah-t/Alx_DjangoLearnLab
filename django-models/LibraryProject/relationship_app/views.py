from django.shortcuts import render
from .models import Library , Book
from django.views.generic.detail import DetailView

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {"books":books}
    return render( request, 'relationship_app/templates/list_books.html', context) 

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/templates/library_detail.html'
    # library = Library.objects.all()
    # for libs in library:
    #     print libs.
