from django.urls import path
from webapp import views


app_name = 'webapp'

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('pic1/',views.pictures,name='pic1'),
    path('pic2/',views.pictures,name='pic2'),
    path('pic3/',views.pictures,name='pic3'),
    path('pictures/',views.pictures,name='pictures'),
]
