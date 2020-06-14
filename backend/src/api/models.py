from django.db import models

class ToDo(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
    
