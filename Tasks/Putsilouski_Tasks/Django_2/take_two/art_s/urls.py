from django.urls import path

from . import views

app_name = "art_s"
urlpatterns =[
    path('', views.index, name = 'index'),
    path('<int:art_id>/', views.detail, name = 'detail'),
    path('<int:art_id>/l_c/', views.l_c, name = 'l_c')
]