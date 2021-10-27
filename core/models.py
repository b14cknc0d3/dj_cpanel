from django.db import models
from time import timezone
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class PriceData(models.Model):
    price = models.IntegerField(null=False,blank=False)
    limit = models.IntegerField(null=False,blank=False)
    # youtube_id= models.CharField(max_length=20,null=False,blank=False)
    # timestamp = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return f'{self.price} | {self.limit}'

class YardData(models.Model):
    yard = models.IntegerField(null=False,blank=False)
    buy = models.ForeignKey(PriceData,related_name="buy",on_delete=models.CASCADE)
    sell = models.ForeignKey(PriceData,related_name="sell",on_delete=models.CASCADE)
    youtube_id= models.CharField(max_length=20,null=False,blank=False)
    timestamp = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.yard}: buy : {self.buy} - sell : {self.sell}"
class Subscribers(models.Model):
    email = models.EmailField(null=False,blank=False,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.email}"
    
    
class BroadCast_Email(models.Model):
    subject = models.CharField(_("Subject"),max_length=225,)
    created = models.DateTimeField(auto_now_add=True)
    message = RichTextField()

    
    def __str__(self) -> str:
        return f'{self.subject}'
    
    class Meta:
        verbose_name = "BroadCast Email to all Subscribers"
        verbose_name_plural = "BroadCast Email"
    
    
