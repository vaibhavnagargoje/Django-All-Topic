from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
 
   # path('',views.index,name='index'),
   path('',views.IdexClassView.as_view(),name='index'),
   
   # path('<int:item_id>/',views.detail,name='detail'),
   # class view for detal
   path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),




   path('item/',views.item,name='item'),

   #add item 
   # path('add/',views.createItem,name='create_item'),
   path('add/',views.CreateItem.as_view(),name='create_item'),


   #update
   path('update/<int:id>/',views.update_item,name="update_item"),

   #delete
   path('delete/<int:id>',views.delete_item,name="delete_item")
   

]
 