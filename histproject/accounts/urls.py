from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include

from histproject.accounts.views import UserRegisterView, EditProfileView, DetailProfileView, DeleteProfileView

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', include([
        path('<int:pk>/edit/', EditProfileView.as_view(), name='profile_edit'),
        path('<int:pk>/', DetailProfileView.as_view(), name='profile_detail'),
        path('<int:pk>/delete/', DeleteProfileView.as_view(), name='profile_delete'),
        path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
        path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    ]))
]