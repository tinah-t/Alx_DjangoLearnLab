
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Article

# Anyone with 'can_view' permission
@permission_required('relationship_app.can_view', raise_exception=True)
def list_articles(request):
    articles = Article.objects.all()
    return render(request, "relationship_app/list_articles.html", {"articles": articles})

# Only users with 'can_create'
@permission_required('relationship_app.can_create', raise_exception=True)
def create_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article.objects.create(
            title=title,
            content=content,
            created_by=request.user
        )
        return render(request, "relationship_app/article_created.html", {"article": article})
    return render(request, "relationship_app/create_article.html")

# Only users with 'can_edit'
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.title = request.POST["title"]
        article.content = request.POST["content"]
        article.save()
        return render(request, "relationship_app/article_updated.html", {"article": article})
    return render(request, "relationship_app/edit_article.html", {"article": article})

# Only users with 'can_delete'
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return render(request, "relationship_app/article_deleted.html")
