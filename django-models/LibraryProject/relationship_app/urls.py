from django.urls import path
from . import views
url_patterns=[
    path('hello/',views.list_books,name='hello'),
    path('about/', views.library_detail.as_view(),name='about')

]