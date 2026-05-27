from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    article_id = models.CharField(20, primary_key=True)
    article_title = models.CharField(20, null=False, default='Шаблон заголовка')
    article_annotation = models.CharField(200, null=False, default='Loren ipsum')
    article_preview_image = models.BinaryField(null=False, default= b'')
    article_text = models.TextField(null=False, default='Loren ipsum')
    creation_date = models.DateTimeField(null=False, default=datetime.now())
    #article_author_id = models.OneToOneField(auth_user, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Article_Picture(models.Model):
    picture_id = models.CharField(20, primary_key=True)
    article_id = models.OneToOneField(Article, on_delete=models.CASCADE)
    picture = models.BinaryField(null=False, default=b'')

    class Meta:
        verbose_name = 'Article_Picture'
        verbose_name_plural = 'Article_Pictures'