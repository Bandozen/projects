from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    contents = models.TextField()
    
    def __str__(self):
        return f"{self.pk}번째 영화 - {self.title}"