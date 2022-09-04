from django.urls import path
from users.views import LoginValidation, RegisterView, RegistrationValidation, LogoutView


app_name = 'users'

urlpatterns = [
    path('validation/', LoginValidation.as_view(), name='login_validation_view'),
    path('register/', RegisterView.as_view(), name='registration_view'),
    path('registration/validation/', RegistrationValidation.as_view(), name='registration_validation_view'),
    path('logout/', LogoutView.as_view(), name='logout'),

]