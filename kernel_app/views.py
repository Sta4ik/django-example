import base64
from django.shortcuts import render
from django.http import HttpResponse
from kernel_app.models import Article, Article_Picture
from kernel_app.forms import New_Article
from random import randint

# Create your views here.
def main_page(request):
    return render(request, "main.html")

def news_page(request):
    newsList = Article.objects.all()
    for news in newsList:
        if news.article_preview_image:
            news.imageBase = base64.b64encode(news.article_preview_image).decode('utf-8')
    return render(request, 'news.html', {'newsList': newsList})

def create_article(request):
    if request.method == 'POST':
        form = New_Article(request.POST, request.FILES)

        if form.is_valid():
            preview = form.cleaned_data['article_preview_image'].read()
            pictures = form.cleaned_data['article_pictures'].read()

            article = Article(article_id = randint(1, 1000000), article_title = form.cleaned_data['article_title'], article_annotation = form.cleaned_data['article_annotation'], 
                              article_preview_image = preview, article_text = form.cleaned_data['article_text'])
            picture_article = Article_Picture(picture_id = randint(1, 1000000), article_id = article, picture = pictures)

            article.save()
            picture_article.save()

    form = New_Article()
    return render(request, 'new_article.html', {"form": form})