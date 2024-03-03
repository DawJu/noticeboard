from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new', views.new, name='new'),
    path('board', views.board, name='board'),
    path('board/<int:id>', views.announcement, name='announcement')
]