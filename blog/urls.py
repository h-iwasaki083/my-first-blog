"path関数とblogアプリのすべてのビューをインポート"
from django.urls import path
from . import views

"最初のurlパターン"
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
