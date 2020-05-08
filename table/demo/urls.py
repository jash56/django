from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('tab', views.tab, name = 'tab'),
]