from django.urls import path

from .import views

app_name = 'blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('posts/<int:pk>/',views.detail,name='detail'),
    path('archives/<int:year>/<int:month>/',views.archive,name='archive'),
    path('category/<int:pk>/',views.category,name='category'),
    path('tag/<int:pk>/',views.tag,name='tag'),
]