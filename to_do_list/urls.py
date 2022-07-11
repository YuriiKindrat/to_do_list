"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from to_do_list_app.views import TagsListView, ToDoListView, TagsCreateView, TagsUpdateView, TagsDeleteView, \
    ToDoCreateView, ToDoDeleteView, ToDoUpdateView, complete_button

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tags/", TagsListView.as_view(), name="tags"),
    path("", ToDoListView.as_view(), name="homepage"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/update/<int:pk>/", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/delete/<int:pk>/", TagsDeleteView.as_view(), name="tags-delete"),
    path("task/create/", ToDoCreateView.as_view(), name="tasks-create"),
    path("task/update/<int:pk>/", ToDoUpdateView.as_view(), name="tasks-update"),
    path("task/delete/<int:pk>/", ToDoDeleteView.as_view(), name="tasks-delete"),
    path("change_status/<int:pk>/", complete_button, name="complete-button"),
]
