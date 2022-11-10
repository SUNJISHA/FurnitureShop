from django.urls import path
from . import views

app_name="exam"
urlpatterns=[

    path('home',views.exam_home,name="home"),
    path('login',views.exam_login,name="login"),
    path('about',views.exam_about,name="about"),
    path('reg',views.exam_reg,name="reg"),
    path('shop',views.exam_shop,name="shop"),
    path('cart',views.exam_cart,name="cart"),
]