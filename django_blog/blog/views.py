from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form':form})
@login_required
def profile_view(request):
    return render(request, "blog/profile.html")

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, "blog/edit_profile.html", {"form": form})


class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/blog_create.html'
    fields = ['title', 'content','author']
    success_url = '/posts/'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/blog_update.html'
    fields = ['title', 'content','author']
    success_url = '/posts/'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/blog_delete.html'
    fields = ['title', 'content','author']
    context_object_name = 'post'
    success_url = '/posts/'
