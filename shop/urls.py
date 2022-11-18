from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name="index"),
     path('contact/', views.contact,name="contacts"),
      path('about/', views.about,name="about"),
       path('search/', views.search,name="search"),
        path('products/<int:myid>', views.productview,name="productview"),
         path('checkout/', views.checkout,name="checkout"),
             
                
]
