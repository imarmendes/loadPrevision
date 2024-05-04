from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('loads/', include('loads.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('register/', include('accounts.urls')),
    path('projects/', include('projects.urls')),
    path('admin/', admin.site.urls),
]
