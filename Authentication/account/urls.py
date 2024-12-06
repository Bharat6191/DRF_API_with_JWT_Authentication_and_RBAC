from django.urls import path
from .views import RegisterView, LoginView, ProjectView, AdminProjectView,LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('projects/', ProjectView.as_view(), name='get_projects'),
    path('projects/create/', AdminProjectView.as_view(), name='create_project'),
    path('logout/', LogoutView.as_view(), name='login'),
]
