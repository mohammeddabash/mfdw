from django.urls import path
from . import views


urlpatterns=[
   # path('',views.index,name="home")
    path('', views.home, name="home"),
    path('about',views.about,name="about"),
    path('contact_us',views.contact_us,name="contact_us"),
    path('our_services',views.our_services,name="our_services"),
    path('<str:pagename>', views.index, name="index"),

]
