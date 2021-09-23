import uuid
import os
from django.db import models
import factory
# Create your models here.
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/news_image/', filename)


def name_random():
    extra={"locale":"en_US"}
    x=factory.Faker('ean', length=10)
    name = factory.Faker("name")
    return name.evaluate_pre(x,10,extra)
    
    
    

class News(models.Model):
    news_image = models.ImageField(upload_to=get_file_path,default="uploads/news_images/default_news.jpg")
    news_title = models.CharField(max_length=100,blank=False,null=False)
    news_body  = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def like_count(self):
        lc = Like.objects.filter(news_id=self.pk,like=True).count()
        return lc
    @property
    def comment_count(self):
        cc = Comment.objects.filter(news_id=self.pk).count()
        return cc

    @property
    def share_count(self):
        sc = Share.objects.filter(news_id=self.pk).count()
        return sc 
    
       
    def __str__(self) -> str:
        return f" {self.id} -{self.news_title} "
    
                #     'ip': request.META.get('REMOTE_ADDR', '')[:63] or None,
                # 'user_agent': \
                #     request.META.get('HTTP_USER_AGENT', '')[:255] \
                #     or None,
    
    
class DeviceID(models.Model):
    name = models.CharField(default=name_random,max_length=30,unique=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent =models.CharField(max_length=225)
    
    def __str__(self) -> str:
        return f"{self.ip_address} {self.user_agent}"
    
    @classmethod
    def update_from_request():
        pass

class Comment(models.Model):
    news_id = models.ForeignKey(News,on_delete=models.CASCADE)
    device_id = models.ForeignKey(DeviceID,on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.device_id} {self.comment}"
    

class Like(models.Model):
    news_id = models.ForeignKey(News,on_delete=models.CASCADE)
    device_id = models.ForeignKey(DeviceID,on_delete=models.CASCADE)
    like = models.BooleanField(default=False,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.device_id} - {self.like}"
    
    class Meta:
        unique_together = ("news_id","device_id")
    
class Share(models.Model):
    news_id = models.ForeignKey(News,on_delete=models.CASCADE)
    device_id = models.ForeignKey(DeviceID,on_delete=models.CASCADE)
    share = models.BooleanField(default=False,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.device_id} - {self.share}"
