from django.urls import path
from .views import posts_list,post_detalhes,user_login,register,post_form,update_post,delete_post
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('detalhes-post/<slug:slug>/', post_detalhes, name='post_detalhes'),
    path('add-post/',post_form, name='post_form'),
    path('update/<slug:slug>/', update_post, name="update_post"),
    path('delete/<slug:slug>/', delete_post, name="delete_post"),
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('register/', register, name='register'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

]
