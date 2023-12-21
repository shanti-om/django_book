from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = \
    [
        # представления поста
        path('', views.post_list, name='post_list'),
        path('about/', views.about, name='about'),
        path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    ]
