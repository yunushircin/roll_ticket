from django.db import models

class CallCenter(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class Problem(models.Model):
    STATUS = (
            ('Açık', 'Açık'), 
            ('Kapalı', 'Kapalı')
            )
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    call_center = models.ForeignKey(CallCenter, null=True, on_delete=models.SET_NULL)

    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)




