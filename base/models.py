from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class Problem(models.Model):
    STATUS = (
            ('Açık', 'Açık'), 
            ('Kapalı', 'Kapalı')
            )
    
    add_by = models.CharField(max_length=20,null=True)
    customer_name = models.CharField(max_length=20,null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.description
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_notifications')
    message = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    

    




