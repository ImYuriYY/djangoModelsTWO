from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    urladdress = models.CharField(max_length=100)
    isPublic = models.BooleanField(default=False)
    category = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.title}'



    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'