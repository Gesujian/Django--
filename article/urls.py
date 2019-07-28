from django.urls import path, re_path
from . import views


app_name = 'article'
urlpatterns =[
        path('article-column', views.article_column,  name="article_column"),
        path('rename-column', views.rename_article_column, name="rename_article_column"),
        path('delete-column', views.delete_column, name="delete_column"),
        path('article-post', views.article_post, name="article_post"),
        path('article-list', views.article_list, name="article_list"),
        path('article-detail/<id>/<slug>/', views.article_detail, name="article_detail"),
        path('list-article-detail/<id>/<slug>/', views.list_article_detail, name="list_article_detail"),
        path('delete-article', views.delete_article, name="delete_article"),
        path('redit-article/<int:article_id>/', views.redit_article, name="redit_article"),
        path('article-titles', views.article_titles, name="article_titles"),
        path('author-article-titles/<username>/', views.article_titles, name="author_article_titles"),
        path('like-article', views.like_article, name="like_article"),
        
]
