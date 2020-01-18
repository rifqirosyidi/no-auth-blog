from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_num = models.IntegerField()

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField()
    slug = models.SlugField()

    def get_update_url(self):
        return f'/posts/{self.slug}/update'

    def get_delete_url(self):
        return f'/posts/{self.slug}/delete'

    def __str__(self):
        return self.title
