from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    article_id = models.CharField(max_length=20, primary_key=True, verbose_name='Индентификатор статьи')
    article_title = models.CharField(max_length=20, null=False, default='Шаблон заголовка', verbose_name='Название статьи')
    article_annotation = models.CharField(max_length=200, null=False, default='Loren ipsum', verbose_name='Аннотация статьи')
    article_preview_image = models.BinaryField(null=False, default=b'', verbose_name='Картинка')
    article_text = models.TextField(null=False, default='Loren ipsum', verbose_name='Текст статьи')
    creation_date = models.DateTimeField(null=False, default=datetime.now, verbose_name='Дата создания')
    #article_author_id = models.OneToOneField(auth_user, on_delete=models.CASCADE)

    def __str__(self):
        return f"Статья {self.article_title}"

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Article_Picture(models.Model):
    picture_id = models.CharField(max_length=20, primary_key=True, verbose_name='Индентификатор изображения')
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Индентификатор статьи')
    picture = models.BinaryField(null=False, default=b'', verbose_name='Изображения')

    def __str__(self):
        return f"Изображения для {self.article_id.article_title}"

    class Meta:
        verbose_name = 'Изображение статьи'
        verbose_name_plural = 'Изображения статьи'