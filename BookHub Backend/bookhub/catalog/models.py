from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_year = models.IntegerField()
    edition = models.CharField(max_length=100)
    description = models.TextField()
    subjects = models.CharField(max_length=255)
    image=models.ImageField(upload_to='image/',default='BookHub/bookapp/src/Images/No_Cover.jpg')


    def __str__(self):
        return self.title
