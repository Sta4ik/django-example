from django.contrib import admin
from django.urls import path
from kernel_app.views import *

urlpatterns = [
    path('', main_page),
    path('home', main_page)
]
