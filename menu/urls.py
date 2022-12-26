from django.urls import path, include, re_path

from menu.views import MenuView, MenuDetailView

urlpatterns = [
    path('', MenuView.as_view(), name='main'),
    re_path(r'^query/([\w/]*)/$', MenuDetailView.as_view(), name='menu_detail'),

]