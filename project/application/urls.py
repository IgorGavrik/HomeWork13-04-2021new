from django.urls import path
from application.views import MainView

urlpatterns = [
    path('home/', MainView.as_view(), name="home"),
    path('add/', MainView.as_view(), name="add")
]