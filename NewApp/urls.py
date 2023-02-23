from django.urls import path
from NewApp import views

urlpatterns=[
    path('',views.home, name='home'),
    path('collections/',views.Collections, name='collections'),
    path('collections/<str:name>',views.Collectionsview, name= 'collectionsview'),
    path('collections/<str:cate>/<str:prod>',views.Productview, name='productview'),
    path('addToCart/<str:cate>/<str:name>/<int:qty>',views.Add_to_cart,name="addToCart"),
    path('cart',views.Cartview,name='cart'),
    path('accessdenied',views.Accessdenied,name='accessdenied'),
    path('update-cart',views.UpdateCart,name='update-cart'),
    path('remove',views.Remove,name='remove'),
]