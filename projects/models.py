from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name #الهدف منها إتاحة استخدام الإسم كسلسلة نصية

class ProjectStatus(models.IntegerChoices):
    #الحروف الكبيرة أستخدمها هنا في البرمجة 
    #الأرقام تتعامل معها قاعدة البيانات
    # الحروف الصغيرة تظهر في التطبيق
    PENDING = 1, 'pending'
    COMPLETED = 2, 'completed'
    POSTPONED = 3, 'postponed'
    CANCELED = 4, 'canceled'

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING
    )
    #العلاقات مع الكيانات الأخرى:
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null =True
        
        
    )

    def __str__(self):
        return self.title

class Task(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description