from os import name
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='Home_Page'),
    path('Addproduct/',views.addpro,name='add_product'),
    path('editproduct/',views.edititem,name='edititem'),
    path('additemm/',views.additem,name='additem'),
    path('edititemm/',views.edititemm,name='edititemm'),
    path('edittheme/<slug:pid>',views.edittheme,name='editdone'),
    path('getfile/',views.getfile,name='getfiletocsv'),
]
