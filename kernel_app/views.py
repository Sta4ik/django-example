import base64
from django.shortcuts import render
from django.http import HttpResponse
from kernel_app.models import Article
from kernel_app.forms import New_Article

# Create your views here.
def main_page(request):
    return render(request, "main.html")

def news_page(request):
    return render(request, 'news.html')

def create_article(request):
    if request.method == 'POST':
        print(request.POST)
    
    form = New_Article()
    return render(request, 'new_article.html', {"form": form})

def imageToBase64(path):
    with open(path, "rb") as image:
        imageStr = base64.b64encode(path.read()).decode("utf-8")
        return imageStr