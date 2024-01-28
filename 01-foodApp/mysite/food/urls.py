from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
 
   path('',views.index,name='index'),
   
   path('<int:item_id>/',views.detail,name='detail'),



   path('item/',views.item,name='item'),

   #add item 
   path('add/',views.createItem,name='create_item'),

   #update
   path('update/<int:id>/',views.update_item,name="update_item"),

   #delete
   path('delete/<int:id>',views.delete_item,name="delete_item")

]
 