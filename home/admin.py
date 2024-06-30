from django.contrib import admin
from .models import ShopList, PDFDatabase, CourseDatabase


admin.site.register(ShopList)
admin.site.register(PDFDatabase)
admin.site.register(CourseDatabase)
