from django.contrib import admin
from .models import University, AdmissionNews, Comment, Discussion, Answer
# Register your models here.

admin.site.register(University)
admin.site.register(AdmissionNews)
admin.site.register(Comment)
admin.site.register(Discussion)
admin.site.register(Answer)
