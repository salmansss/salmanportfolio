from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path('voting/', views.voting, name='voting'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('pinggame/', views.pinggame, name='pinggame'),
    path('textutils/', views.textutils, name='textutils'),
    path('sportcenter/', views.sportcenter, name='sportcenter'),
]