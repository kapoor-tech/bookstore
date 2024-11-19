from django.db import models # type: ignore

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amazon_url = models.URLField()  # URL to the book's Amazon page

    def __str__(self):
        return self.title