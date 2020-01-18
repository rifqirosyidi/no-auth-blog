from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'posts'

urlpatterns = [
    path('posts/', views.posts_list, name='list'),
    path('posts/create/', views.posts_create, name='create'),
    path('posts/<slug:slug>/update/', views.posts_update, name='update'),
    path('posts/<slug:slug>/delete', views.posts_delete, name='delete'),

    path('posts/<slug:slug>/', views.posts_detail, name='detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)