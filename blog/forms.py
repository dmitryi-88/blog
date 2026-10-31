from django import forms
from .models import Post, Author, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "name",
            "describe",
            "text",
            "category",
            "author",
            "image",
        )


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = (
            "name",
            "birthday",
            "biography",
            "image",
        )
        widgets = {
            "birthday": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d",
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
