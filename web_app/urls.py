from django.urls import path, re_path
from web_app import views

# app url 配置
urlpatterns = [
    path('',views.index,name='index'),
]