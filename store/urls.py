from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.store,name='store'),
    path('category/<slug:slug>',views.store,name='product_by_category'),
    path('category/<slug:slug1>/<slug:slug2>',views.product_details,name='product_details'),
    path("search/",views.search,name='search')
]