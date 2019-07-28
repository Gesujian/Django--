from django.urls import path, include
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.blog_title, name="blog_title"),
    path("<article_id>/",views.blog_article),
]
