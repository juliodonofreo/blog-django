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
    path('', views.PostListView.as_view(), name="index"),
    path('page/<slug:slug>/', views.PageDetailView.as_view(), name="page"),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name="post"),
    path(
        'created_by/<int:author_id>/', views.CreatedByListView.as_view(),
        name="author"),
    path('category/<slug:slug>/', views.CategoryListView.as_view(),
         name="category"),
    path('tag/<slug:slug>/', views.TagListView.as_view(), name="tag"),
    path('search/', views.SearchListView.as_view(), name="search"),
]
