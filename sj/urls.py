"""sj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from os import name
from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="urlhome"),
    path('new/', views.new, name="urlnew"),
    path('<str:idid>', views.detail, name="urldetail"),
    path('create/', views.create, name="urlcreate"),
    path('edit<str:idid>/', views.edit, name="urledit"),
    path('update<str:idid>/', views.update, name="urlupdate"),
    path('delete<str:idid>/', views.delete, name="urldelete"),
    path('account/', include('account.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
