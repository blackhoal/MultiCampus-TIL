from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('hola/', views.hola),
    path('dinner/', views.dinner),
    path('hello/<name>/', views.hello),
    path('introduce/<name>/<int:age>/', views.introduce),
    path('times/<int:a>/<int:b>/', views.times),
    path('circle/<int:r>', views.circle),
    path('template_language/', views.template_language),
    path('birthday/', views.birthday),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto/', views.Lotto),
    path('get/', views.get),
    path('lotto2/', views.Lotto2),
    path('winnum/', views.winnum),
    path('art/', views.art),
    path('masterpiece/', views.masterpiece),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
