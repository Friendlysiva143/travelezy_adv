from django.urls import path
from . import views
urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('',views.dashboard,name='dashboard'),
    path('forgetpassword/',views.forgetpassword,name='forgetpassword'),
    path('resetpassword/',views.resetpassword,name='resetpassword'),


    
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
    path('resetpassword_validate/<uidb64>/<token>/',views.resetpassword_validate,name='resetpassword_validate')

]