from django.urls import path    
from blog.views import blog_view ,blog_single, blog_category , blog_search


app_name = 'blog'

urlpatterns = [
    path('',blog_view, name='index'),
    path('<int:pid>',blog_single, name='single'),
    path('category/<str:cat_name>',blog_category , name='category'),
    path('author/<str:author_username>',blog_view, name = 'author'),
    path('search/',blog_search, name ='search'),
    path('tag/<str:tag_name>/', blog_view, name='tag')

]
