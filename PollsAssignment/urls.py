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
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include(('Polls.urls', 'Polls'), namespace="Polls")),

    # path('polls/game/', GamePage, name='Front'),
    # path('polls/<int:pk>/', ChoicePage, name='detail'),
    # url(r'^polls/', VoteCount, name='Vote'),
]
