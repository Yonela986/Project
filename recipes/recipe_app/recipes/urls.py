from django.urls import path
from .views import register, recipe_list

urlpatterns = [
    path('register/', register, name='register'),
    path('list/', recipe_list, name='recipe_list'),  

]