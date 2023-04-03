from django.urls import path
from app import views

urlpatterns = [
    path('', views.Homeview, name='home'),
    path('detail/<str:pk', views.DetailView, name='detail'),
    path('update/<str:pk>', views.UpdateView, name='update'),
    path('create/', views.CreateView, name='create'),
]
