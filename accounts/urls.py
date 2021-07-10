from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/',views.userPage,name='user-page'),
    path('employee/',views.employeePage,name='employee-page'),
    path('manager/',views.managerPage,name='manager-page'),
    path('account/',views.accountSettings,name="account"),
    path('accountstaff/',views.accountSettingsEmployees,name="accountstaff"),

    path('', views.home,name="home"),
    path('customer/<int:id>/',views.customer,name="customer" ),
    path('createnewrental/<int:id>/',views.createNewRental,name="createnewrental" ),
    path('pie-chart/', views.pie_chart, name='pie-chart'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    path('password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), 
     name="password_reset_confirm"),

    path('reset/done/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), 
        name="password_reset_complete"),

    path("password_reset", views.password_reset_request, name="password_reset"),          




]
