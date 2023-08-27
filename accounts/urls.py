from django.conf.urls import url
from django.urls import path

from . import views
from django.contrib.auth import views as authviews

urlpatterns = [
    path('signup', views.signup, name='signup'),
   # path('accounts',views.index,name='accounts')
    #url('login', authviews.LoginView.as_view(template_name='accounts/login.html'), name='login'),

   # url('', views.index, name='signup'),
    #url('sign_up', views.signup, name='signup'),


]