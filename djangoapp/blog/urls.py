"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from blog import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    path('', views.index, name="index"),
    path('page/<slug:slug>/', views.page, name="page"),
    path('post/<slug:slug>/', views.post, name="post"),
    path('created_by/<int:author_id>/', views.created_by, name="author"),
    path('category/<slug:slug>/', views.category, name="category"),

]
