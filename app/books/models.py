from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    upload_date = models.DateField(auto_now=True,blank=True)
    updated_date = models.DateField(auto_now=True,blank=True)
    release_date = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title} - {self.author}"


class Comment(models.Model):
    book = models.ForeignKey(
        Book, related_name="comments", on_delete=models.CASCADE)
    commentor = models.ForeignKey(User,related_name="commenter", on_delete=models.CASCADE)
    comment = models.TextField()
    upload_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    evaluation = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.book} / -> {self.commentor}"
