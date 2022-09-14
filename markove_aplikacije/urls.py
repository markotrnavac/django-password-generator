"""markove_aplikacije URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from pocetna import views as pocetna_views
from generator import views as generator_views
from palindrom import views as palindrom_views
from wordcount import views as wordcount_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pocetna_views.home, name="home"),
    path('generator', generator_views.home, name="generator"),
    path('password/', generator_views.password, name='password'),
    # path('about/', generator_views.about, name='about'),
    path('palindrom/', palindrom_views.palindrom, name='palindrom'),
    path('palout/', palindrom_views.palout, name='palout'),
    path('wordcount/', wordcount_views.wordcount, name='wordcount'),
    path('wordcountout/', wordcount_views.wordcountout, name='wordcountout'),
    path('about/', generator_views.about, name='about'),

]
