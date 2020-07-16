from django.urls import path
from django_app import views

app_name = 'django_app'

urlpatterns = [ path('register/', views.register,name='register'),
                path('login/', views.user_login,name='user_login'),
                ]
