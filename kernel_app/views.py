import base64
from django.shortcuts import render, get_object_or_404, redirect
from kernel_app.models import Article, Article_Picture
from kernel_app.forms import New_Article, LoginForm
from random import randint
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def main_page(request):
    return render(request, "main.html")

@login_required
def news_page(request):
    newsList = Article.objects.all()
    for news in newsList:
        if news.article_preview_image:
            news.imageBase = base64.b64encode(news.article_preview_image).decode('utf-8')
    return render(request, 'news.html', {'newsList': newsList})

@login_required
def create_article(request):
    if request.method == 'POST':
        form = New_Article(request.POST, request.FILES)

        if form.is_valid():
            preview = form.cleaned_data['article_preview_image'].read()
            pictures = form.cleaned_data['article_pictures']

            article = Article(article_id = str(randint(1, 1000000)), article_title = form.cleaned_data['article_title'], article_annotation = form.cleaned_data['article_annotation'], 
                              article_preview_image = preview, article_text = form.cleaned_data['article_text'])
            article.save()

            for p in pictures:
                picture_article = Article_Picture(picture_id = str(randint(1, 1000000)), article_id = article, picture = p.read())
                picture_article.save()
            
    form = New_Article()
    return render(request, 'new_article.html', {"form": form})

@login_required
def article_page(request, article_id):
    news = get_object_or_404(Article, article_id=article_id)
    pictures = Article_Picture.objects.filter(article_id=news)

    picturesList = []
    for picture in pictures:
        pictureBase64 = base64.b64encode(picture.picture).decode('utf-8')
        picturesList.append(pictureBase64)

    return render(request, 'news_detail.html', {"news": news, "picturesList": picturesList})

def page404(request):
    return render(request, '404.html')

def login_page(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('news')
    return render(request, 'login.html', {'form': form})

def logout_page(request):
    logout(request)
    return redirect('login')