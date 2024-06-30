from django.db import models
from django.db.models.fields.files import ImageField

class ShopList (models.Model):
    shopkeeper = models.CharField (max_length=99, null=True, blank=True)
    username = models.CharField (max_length=99, null=True, blank=True)
    shopname = models.CharField (max_length=99, null=True, blank=True)
    shoplocation = models.CharField (max_length=99, null=True, blank=True)
    description = models.TextField (null=True, blank=True)
    shopphoto=ImageField(upload_to='shop_photo/', null = True, blank = True)

    def __str__(self):
        if len(self.shopname) > 50:
            return self.shopname[:50]+"..."
        return self.shopname
    
class PDFDatabase (models.Model):
    senderusername = models.CharField(max_length=99, null=True, blank=True)
    sendername = models.CharField(max_length=99, null=True, blank=True)
    senderemail = models.CharField(max_length=99, null=True, blank=True)
    senderphone = models.CharField(max_length=99, null=True, blank=True)
    selectedshopusername = models.CharField(max_length=99, null=True, blank=True)
    selectshopname = models.CharField(max_length=99, null=True, blank=True)
    file = models.FileField(upload_to='file/', null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.BooleanField(default = False)
    total_page = models.IntegerField(null=True, blank=True)
    total_cost = models.IntegerField(null=True, blank=True)
    transaction = models.CharField(max_length=99, null=True, blank=True)
    payment_status = models.BooleanField(default = False)

    def __str__(self):
        if len(self.sendername) > 50:
            return self.sendername[:50]+"..."
        return self.sendername
    
class CourseDatabase (models.Model):
    course_type = models.CharField(max_length=99, blank=True, null=True)
    course_name = models.CharField(max_length=99, null=True, blank=True)
    short_description = models.CharField(max_length=99, null=True, blank=True)
    instructor = models.CharField(max_length=99, null=True, blank=True)
    syllabus = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=99, null=True, blank=True)

    def __str__(self):
        if len(self.course_name) > 50:
            return self.course_name[:50]+"..."
        return self.course_name
