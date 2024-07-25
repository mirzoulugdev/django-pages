from django.urls import path
from .views import HomePageView, AboutPageView, CoursePageView, AdresspageView



urlpatterns = [
    path('', HomePageView.as_view(), name= 'home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('course/', CoursePageView.as_view(), name='course'),
    path('adress/', AdresspageView.as_view(), name='adress')
  
]