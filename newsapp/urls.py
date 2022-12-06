from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    # path('login/',views.user_login,name='login')
    path('',views.landing,name='index'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/<title>/',views.detail,name='detail'),
    path('trending/',views.trending,name='trending'),
    path('register/',views.register,name='register'),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('edit/',views.edit,name='edit'),
    path('invite_friends/',views.invite_friends,name='invite_friends'),
    path('users/',views.user_list,name='user_list'),
    path('users/follow/',views.user_follow,name='user_follow'),
    path('users/<username>/',views.user_detail,name='user_detail'),

    #path('submit_rating/<int:article_id>/',views.submit_rating,name='submit_rarting'),

]
