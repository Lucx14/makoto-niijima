from django.urls import path

from .views import ArticleIndex, ArticleDetail, ArticleCreate, ArticleUpdate, ArticleDelete

urlpatterns = [
    path("", ArticleIndex.as_view(), name="articles"),
    path("article/<int:pk>/", ArticleDetail.as_view(), name="article"),
    path("article/new/", ArticleCreate.as_view(), name="article-new"),
    path("article/<int:pk>/edit/", ArticleUpdate.as_view(), name="article-edit"),
    path("article/<int:pk>/delete", ArticleDelete.as_view(), name="article-delete"),
]
