from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('adios/', views.adios),
    path('dinner/', views.dinner),
    path('hello/<name>/', views.hello),
    path('introduce/<name>/<int:age>', views.introduce),
    path('times/<int:num1>/<int:num2>', views.times),
    path('circle/<int:r>', views.circle),
    path('template_language', views.template_language),
    path('birthday', views.birthday),
    path('throw', views.throw),
    path('catch/', views.catch),
    path('lottoinput', views.lottoinput),
    path('lottooutput/', views.lottooutput),
]
