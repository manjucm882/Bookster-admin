from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 150, unique=True ,db_index=True)
    
    

    def __str__(self):
        return self.name
    
class language_written(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Writer(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 150, unique=True ,db_index=True)
    bio = models.TextField()
    pic = models.FileField(upload_to="writer/")

    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=150)
    writer = models.ForeignKey(Writer, on_delete = models.CASCADE)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    language = models.ForeignKey(language_written,on_delete=models.CASCADE)
    min_age = models.IntegerField()
    slug = models.SlugField(max_length=100, db_index=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    coverpage = models.FileField(upload_to = "coverpage/")
    bookpage = models.FileField(upload_to = "bookpage/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    totalreview = models.IntegerField(default=1)
    totalrating = models.DecimalField(max_digits=5,decimal_places=1)
    status = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
	customer = models.ForeignKey(User, on_delete = models.CASCADE)
	book = models.ForeignKey(Book, on_delete = models.CASCADE)
	review_star = models.IntegerField()
	review_text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

class Slider(models.Model):
	title = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slideimg = models.FileField(upload_to = "slide/")

	def __str__(self):
		return self.title