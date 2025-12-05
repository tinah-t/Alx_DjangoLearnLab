from django import forms
from .models import Post, Comment, Tag


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'})
        }

class PostForm(forms.ModelForm):
    # Comma-separated tags: "django, python, api"
    tags = forms.CharField(required=False, help_text="Add tags separated by commas")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()

        # Process tags
        tag_text = self.cleaned_data["tags"]
        tag_list = [t.strip() for t in tag_text.split(",") if t.strip()]

        post.tags.clear()
        for tag_name in tag_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)

        return post
