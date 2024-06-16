
from django.urls import path
from . import views


urlpatterns = [
     path('userlist/',views.userlist,name="userlist"),
     path('userdetails/<int:book_id>/',views.userdetails,name="userdetails"),
     path('usersearch/',views.usersearch,name="usersearch"),
     path('index/',views.index),
     path('logout/',views.logout,name='logout'),
     path('add_to_cart/<int:book_id>/',views.add_to_cart,name="addtocart"),
     path('viewcart/',views.view_cart,name='viewcart'),
     path('increase/<int:item_id>',views.increase_quantity,name="increase_quantity"),
     path('decrease/<int:item_id>', views.decrease_quantity, name="decrease_quantity"),
     path('remove/<int:item_id>',views.remove_from_cart,name="remove_cart"),
     path('create_checkout_session',views.create_checkout_session,name="create_checkout_session"),
     path('success',views.success,name="success"),
     path('cancel',views.cancel,name="cancel")

]