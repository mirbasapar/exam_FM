from django.db import models

class Motto(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Video(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Gadget(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    popularity = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, related_name='gadgets')

    def __str__(self):
        return self.name

class Review(models.Model):
    gadget = models.ForeignKey(Gadget, related_name='reviews', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f'Review by {self.author} on {self.gadget.name}'





