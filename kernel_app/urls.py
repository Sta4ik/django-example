from django.contrib import admin
from django.urls import path
from kernel_app.views import *
from django.views.generic import DetailView

urlpatterns = [
    path('', main_page),
    path('home', main_page),
    path('news', news_page),
    path('new', create_article),
    path('news/<str:article_id>/', DetailView.as_view(model=Article, slug_field='article_id', slug_url_kwarg='article_id', 
                                                      template_name='news_detail.html', context_object_name='news',))
]
