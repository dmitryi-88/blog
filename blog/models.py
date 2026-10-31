from django.db import models
from django.conf import settings


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(
        verbose_name="Название",
        max_length=100,
        unique=True,
    )
    describe = models.TextField(
        verbose_name="Описание",
        blank=True,
    )

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    class Meta:
        verbose_name = "Автор произведения"
        verbose_name_plural = "Авторы произведения"

    name = models.CharField(
        verbose_name="Имя автора",
        max_length=100,
    )
    birthday = models.DateField(
        verbose_name="Дата рождения",
        blank=True,
        null=True,
    )
    biography = models.TextField(
        verbose_name="Биография",
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Фото",
        blank=True,
        null=True,
        upload_to="authors_images/",
    )
    writer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Добавил пользователь",
        on_delete=models.CASCADE,
        related_name="added_authors",
    )

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ["-create_at"]

    name = models.CharField(
        verbose_name="Название",
        max_length=100,
    )
    describe = models.CharField(
        verbose_name="Описание",
        max_length=255,
        blank=True,
    )
    text = models.TextField(
        verbose_name="Текст",
    )
    create_at = models.DateTimeField(
        verbose_name="Дата написания",
        auto_now_add=True,
    )
    update_at = models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="posts",
        verbose_name="Категория",
    )
    author = models.ManyToManyField(
        to=Author,
        related_name="posts",
        verbose_name="Авторы произведения",
    )
    is_published = models.BooleanField(
        verbose_name="Опубликовано",
        default=True,
    )
    image = models.ImageField(
        verbose_name="Фото",
        blank=True,
        null=True,
        upload_to="post_images/",
    )
    writer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор публикации",
    )

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-create_at",)

    text = models.TextField(
        verbose_name="Комментарий",
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Публикация",
    )
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    writer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пользователь",
    )

    def __str__(self) -> str:
        return f'Комментарий пользователя {self.writer} к публикации "{self.post}"'
