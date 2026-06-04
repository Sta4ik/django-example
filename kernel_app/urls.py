from django.contrib import admin
from django.urls import path
from kernel_app.views import *
from django.views.generic import DetailView

urlpatterns = [
    path('', main_page),
    path('home', main_page),
    path('news', news_page, name='news'),
    path('new', create_article, name='new'),
    path('news/<str:article_id>/', article_page),
    path('404', page404),
    path('login', login_page, name='login'),
    path('logout', logout_page)
]