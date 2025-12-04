from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post
from django import forms
# Create your views here.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

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

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = '/posts/'
    def form_valid(self, form):
        form.instance.author = self.request.user  # Auto-set author
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'
    success_url = '/posts/'
    def form_valid(self, form):
        form.instance.author = self.request.user  # Auto-set author
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    fields = ['title', 'content','author']
    context_object_name = 'post'
    success_url = '/posts/'
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author