from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('utilities/', include('utilities.urls')),
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls'))
]