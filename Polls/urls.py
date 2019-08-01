"""PollsAssignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Polls.views import *
from django.conf.urls import url
from . import views

app_name='Polls'

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    path('',views.FirstPage, name='First'),
    path('game/', GamePage, name='Front'),
    path('<int:pk>/question',views.questionList.as_view(),name='list'),
    path('<int:pk>/', views.QuestionView, name='que'),
    path('<int:pk>/result/', views.ResultView, name='result'),
    path('<int:pk>/<str:name>/track',views.crudTrack.as_view(),name='track'),
    path('<int:pk>/<str:name>/track',views.crudTrack.as_view(),name='track'),

    #url('<int:question_id>/vote/', vote_count, name='vote_detail'),
    # url(r'^(?P<question_id>\d+)/vote/$', vote_count, name='vote_detail'),
]

# urlpatterns = [
#
    # path('game/', GamePage, name='Front'),
    # path('polls/<int:pk>/', ChoicePage, name='detail'),
    # url(r'polls/<int:pk>/vote', VoteCount, name='Vote'),
# ]