from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/', views.report_issue, name='report'),
    path('track/', views.track_issues, name='track'),
    path('view/', views.view_issues, name='view'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('offices/', views.offices, name='offices'),
    path('logout/', views.logout_view, name='logout'),
]