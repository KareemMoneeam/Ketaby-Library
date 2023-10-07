from django.db import models

class category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Book(models.Model):

    status_book=[
        ('available','available'),
        ('borrowed','borrowed'),
        ('sold','sold')
    ]
   
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True,blank=True)
    photo_book = models.ImageField(upload_to='photos',null=True,blank=True)
    pages = models.IntegerField(null=True,blank=True)
    borrowing_days = models.IntegerField(null=True,blank=True)
    active = models.BooleanField(default= True)
    status = models.CharField(max_length=50, choices=status_book , null=True,blank=True)
    category = models.ForeignKey(category, on_delete=models.PROTECT, null=True,blank=True)
    def __str__(self):
            return self.title

   