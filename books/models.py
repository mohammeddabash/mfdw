from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
# Create your models here.
class book(models.Model):
    book_name=models.CharField(max_length=40)
    book_describtion=models.TextField(max_length=120)
    book_photo=models.ImageField(blank=True,upload_to='images/',default='static/logo.jpg')
    book_price=models.IntegerField(null=True,default=20)
    file=models.FileField(blank=True,upload_to='files/')
    uploader_paypal_email=models.CharField(max_length=120,)
    choices=(
         ('books','books'),
         ('records','records'),
         ('lectures','lectures'),
    )
    book_category=models.CharField(max_length=40,blank=True,choices=choices,default='book')
    pub_date=models.DateTimeField(blank=True,null=True,default=timezone.now())

    def __str__(self):
        return self.book_name
    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=30) <= self.pub_date <= timezone.now()

    def year(self,year):
        return self.pub_date.strftime('%Y')==str(year)
    def category(self,category):
        return self.book_category==category
