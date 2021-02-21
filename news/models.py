from django.db import models
from tinymce.models import HTMLField


class MainCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Main Category"


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class News(models.Model):
    main_category = models.ForeignKey(
        MainCategory, on_delete=models.CASCADE, null=False)
    category = models.ManyToManyField(Category, related_name="category")
    news_title = models.CharField(max_length=200)
    news_text = HTMLField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name_plural = "News"
