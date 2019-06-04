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
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto/', views.lotto),
    path('get/', views.get),
    path('lotto2/', views.lotto2),
    path('picklotto/', views.picklotto),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
