# from time import thread_time
import threading
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import BroadCast_Email, PriceData, Subscribers, YardData
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import (send_mail, BadHeaderError, EmailMessage)
# Register your models here.
admin.site.site_header = "DummyCrypto Administration"
admin.site.site_title = "DummyCrypto"



class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.html_content = html_content
        self.recipient_list = recipient_list
        threading.Thread.__init__(self)
        
    def run(self) -> None:
        msg = EmailMessage(
            self.subject,self.html_content,
            settings.EMAIL_HOST_USER,
            self.recipient_list
        )
        msg.content_subtype = "html"
        try:
            msg.send()
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
            
        # return super().run()
        
    
class BroadCastEmailAdmin(admin.ModelAdmin):
    model = BroadCast_Email
    
    def submit_email(
        self,request,obj
    ):
        list_email = [s.email for s in Subscribers.objects.all()]
        obj_selected =obj[0]
        EmailThread(obj_selected.subject,mark_safe(obj_selected.message),list_email).start()
        
    submit_email.short_description = "Submit BroadCast (select only)"
    submit_email.allow_tag = True
    actions =['submit_email']
    list_display = ("subject","created")
    search_fields = ("subject",)

admin.site.register(PriceData)
admin.site.register(YardData)
admin.site.register(Subscribers)
admin.site.register(BroadCast_Email,BroadCastEmailAdmin)
