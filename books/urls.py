from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name="home"),
    path('search',views.HomePageView.as_view(),name="search"),
    path('search_results',views.SearchResultsView.as_view(),name="search_results"),
    path('create', views.create, name='create'),
    path('<int:id>/payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    path('<str:category>' '/' '<int:year>', views.category_year_filter, name="category_years"),
    path('<int:year>', views.year_filter, name="year_filter"),
    path('b<int:id>', views.thing, name="thing"),
    path('<str:pagename>', views.another, name="index"),
    #path('', views.home, name="home"),
    #path('about', views.about, name="about"),
   # path('contact_us', views.contact_us, name="contact_us"),
    #path('our_services', views.our_services, name="our_services"),

]
