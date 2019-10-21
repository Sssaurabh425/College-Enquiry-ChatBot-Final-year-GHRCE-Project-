from django.conf.urls import url
from . import views

urlpatterns = [ url(r'^$', views.chatbot, name='ChatBot'),
                url(r'^ajax/answer/$', views.answer, name='answer')]