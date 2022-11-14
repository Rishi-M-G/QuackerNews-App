# ***********************Delete this later*******************************
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# ***********************************************************************

# ***********************Delete this later*******************************
urlpatterns = [
    #post views
    # path('login/',views.user_login,name='login'),
    path ('login/',auth_views.LoginView.as_view(),name='login'),
    path ('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path ('',views.dashboard,name='dashboard'),
    path('register/',views.register,name='register'),
    path('edit/',views.edit,name='edit'),
    # path('',views.dashboard,name='dashboard')
]
# ***********************************************************************