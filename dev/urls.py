from django.urls import path
from dev import views
urlpatterns=[
    path('',views.home,name="home"),
    path('login',views.loginm,name="login"),
    path('register',views.register,name="register"),
    path('post',views.post,name="post"),
    path('profile',views.profile,name="pofile"),
]