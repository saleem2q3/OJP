from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('employerhomepage', views.employerhomepage, name='employerhomepage'),
    path('jobseekerhomepage', views.jobseekerhomepage, name='jobseekerhomepage'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('signup1', views.signup1, name='signup1'),
    path('login', views.login1, name='login'),
    path('login1', views.login1, name='login1'),
    path('logout', views.logout, name='logout'),
    path('company', views.company, name='company'),
    path('read', views.read, name='read'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_homepage/', views.admin_homepage, name='admin_homepage'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('account_details', views.account_details, name='account_details'),
    path('user_application_dashboard/', views.user_application_dashboard, name='user_application_dashboard'),
    path('delete/<int:application_id>/', views.delete_job_application, name='delete_application'),
    path('confirm_delete/<int:application_id>/', views.confirm_delete_application, name='confirm_delete_application'),
    path('application/<int:application_id>/accept/', views.accept_job_application, name='accept_job_application'),
    path('application/<int:application_id>/confirm_accept/', views.confirm_accept_application,
         name='confirm_accept_application'),
    # other URL patterns

    path('user_profile', views.user_profile, name='user_profile'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
