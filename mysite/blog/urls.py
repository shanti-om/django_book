from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = \
    [
        # представления поста
        path('about/', views.about, name='about'),
        path('more/', views.more, name='more'),
        path('', views.post_list, name='post_list'),
        path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
        path('category/<int:category_id>/', views.category_id, name='category_id'),
        path('category/<slug:category_slug>/', views.category_slug, name='category_slug'),

    ]
