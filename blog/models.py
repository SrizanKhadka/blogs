from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Blogs(models.Model):
    blog_writer = models.CharField(max_length=100)
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name="category", default=1)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.blog_writer} - {self.blog_title}'