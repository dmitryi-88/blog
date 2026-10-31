from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("<int:pk>/update/", views.PostUpdateView.as_view(), name="post_update"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("<int:pk>/comment/", views.CommentCreateView.as_view(), name="add_comment"),
    path("authors/", views.AuthorListView.as_view(), name="author_list"),
    path("authors/create/", views.AuthorCreateView.as_view(), name="author_create"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author_detail"),
    path(
        "authors/<int:pk>/update/",
        views.AuthorUpdateView.as_view(),
        name="author_update",
    ),
    path(
        "authors/<int:pk>/delete/",
        views.AuthorDeleteView.as_view(),
        name="author_delete",
    ),
    path("search/", views.PostSearchView.as_view(), name="post_search"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path(
        "categories/<int:pk>/",
        views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
]
