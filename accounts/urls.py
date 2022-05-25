from django.urls import path,include
from . import views
from .views import login_view,logout_view,signup_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("",views.post,name="posts")
    path("login/",login_view, name="login"),
    path("dashboard/",views.dashboard, name="dashboard"),
    path("logout/",logout_view, name="logout"),
    path("signup/",signup_view, name="signup"),
    path("profile/",views.profile, name="profile"),
    # path("edit-profile/",views.edit_profile, name="edit_profile"),
    # path("update-profile/",views.update_profile, name="update_profile"),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path("password_reset/",auth_views.PasswordResetView.as_view(),name='password_reset'),
    path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]

