from django.urls import path

from .views import (
    ArticleIndex,
    ArticleDetail,
    ArticleCreate,
    ArticleUpdate,
    ArticleDelete,
    CustomLoginView,
    CustomLogoutView,
    SignUpView,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name='signup'),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("", ArticleIndex.as_view(), name="articles"),
    path("article/<int:pk>/", ArticleDetail.as_view(), name="article"),
    path("article/new/", ArticleCreate.as_view(), name="article-new"),
    path("article/<int:pk>/edit/", ArticleUpdate.as_view(), name="article-edit"),
    path("article/<int:pk>/delete", ArticleDelete.as_view(), name="article-delete"),
]
