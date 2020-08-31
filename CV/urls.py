from django.urls import path
from . import views

urlpatterns = [

    path('', views.home_view, name='homepage'),
    path('editCV/', views.edit_CV, name="edit_CV")

]
