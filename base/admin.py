from django.contrib import admin
from .models import Article, Comment, Like
from django.db.models import Model
from django.shortcuts import resolve_url
from django.utils.safestring import SafeText
from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.utils.html import format_html


def model_admin_url(obj: Model, name: str = None) -> str:
    url = resolve_url(admin_urlname(obj._meta, SafeText("change")), obj.pk)
    return format_html(f'<a href="{url}">{name or str(obj)}</a>')


class CommentInline(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "published",
        "link_to_user_admin",
        "likes_count",
        "created_at",
    )
    fieldsets = [
        (None, {"fields": ["author", "published"]}),
        ("Article Content", {"fields": ["title", "body", "image"]}),
    ]
    inlines = [CommentInline]

    @admin.display(description="Author")
    def link_to_user_admin(self, obj):
        return model_admin_url(obj.author)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "link_to_article_admin",
        "link_to_user_admin",
        "content",
        "likes_count",
        "created_at",
    )

    @admin.display(description="Article")
    def link_to_article_admin(self, obj):
        return model_admin_url(obj.article)

    @admin.display(description="Author")
    def link_to_user_admin(self, obj):
        return model_admin_url(obj.author)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)
