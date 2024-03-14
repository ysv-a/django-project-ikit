from django.db import models

# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Tag(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Article(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag, empty_label=None)
    name = models.CharField(max_length=255, verbose_name="Имя")
    description = models.TextField(verbose_name="Описание")
    characters = models.IntegerField(verbose_name="Количество страниц")
    featured_image = models.ImageField(blank=True, default="default.jpg", upload_to="images/")
    # pub_date = models.DateTimeField(verbose_name="Дата публикации")
    # is_active = models.BooleanField(blank=True, default=True)

    # class Meta:
    #     ordering = ["name"]
    #     indexes = [
    #         models.Index(fields=["name"], name="article_index_name"),
    #     ]

    def __str__(self):
        return f"{self.name}"
