from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, db_index=True)
    category_pretty_name = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.category_name


class Word(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.category.category_name + ':' + self.word
