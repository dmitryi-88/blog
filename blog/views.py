from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Author, Comment, Category
from .forms import CommentForm, PostForm, AuthorForm


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 4

    def get_queryset(self):
        return (
            Post.objects.filter(is_published=True)
            .select_related("category")
            .prefetch_related("author")
            .order_by("-create_at")
        )


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return (
            Post.objects.filter(is_published=True)
            .select_related("category", "writer")
            .prefetch_related("author", "comments__writer")
        )


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "blog:post_detail",
            kwargs={"pk": self.object.pk},
        )


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(writer=self.request.user)

    def get_success_url(self):
        return reverse(
            "blog:post_detail",
            kwargs={"pk": self.object.pk},
        )


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("blog:post_list")

    def get_queryset(self):
        return Post.objects.filter(writer=self.request.user)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.instance.post_id = self.kwargs["pk"]

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.kwargs["pk"]})


class AuthorListView(ListView):
    model = Author
    template_name = "blog/author_list.html"
    context_object_name = "authors"
    paginate_by = 4

    def get_queryset(self):
        return Author.objects.prefetch_related("posts").order_by("name")


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "blog/author_form.html"

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:author_list")


class AuthorDetailView(DetailView):
    model = Author
    template_name = "blog/author_detail.html"
    context_object_name = "author"

    def get_queryset(self):
        return Author.objects.prefetch_related("posts")


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "blog/author_form.html"
    context_object_name = "author"

    def get_queryset(self):
        return Author.objects.filter(writer=self.request.user)

    def get_success_url(self):
        return reverse("blog:author_detail", kwargs={"pk": self.object.pk})


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = "blog/author_confirm_delete.html"
    context_object_name = "author"
    success_url = reverse_lazy("blog:author_list")

    def get_queryset(self):
        return Author.objects.filter(writer=self.request.user)


class PostSearchView(ListView):
    model = Post
    template_name = "blog/post_search.html"
    context_object_name = "posts"

    def get_queryset(self):
        query = self.request.GET.get("q", "")

        return (
            Post.objects.filter(is_published=True, name__icontains=query)
            .select_related("category")
            .prefetch_related("author")
            .order_by("-create_at")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


class CategoryListView(ListView):
    model = Category
    template_name = "blog/category_list.html"
    context_object_name = "categories"
    paginate_by = 4

    def get_queryset(self):
        return Category.objects.order_by("name")


class CategoryDetailView(DetailView):
    model = Category
    template_name = "blog/category_detail.html"
    context_object_name = "category"

    def get_queryset(self):
        return Category.objects.prefetch_related("posts")
