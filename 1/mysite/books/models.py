from django.db import models
# Create your models here.
#modified for lab4
class Author(models.Model):
    AuthorID = models.CharField(max_length = 30)
    Name = models.CharField(max_length = 40)
    Age = models.CharField(max_length = 10)
    Country=models.CharField(max_length = 30)
    def __unicode__(self):
        return self.Name
class Book(models.Model):
    ISBN = models.CharField(max_length = 100)
    Title = models.CharField(max_length = 100)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 40)
    PublishDate = models.DateField()
    Price = models.CharField(max_length = 80)
    def __unicode__(self):
       return self.Title
