from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('boards/', include("boards.urls")),
    path('admin/', admin.site.urls),
]
