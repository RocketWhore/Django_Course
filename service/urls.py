from django.urls import path
from service.views import HomeView, ClientListView, MessageListView, ClientCreateView, ClientDeleteView, \
    ClientUpdateView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, ActivateMessage
from service.apps import ServiceConfig
from django.views.decorators.cache import cache_page

app_name = ServiceConfig.name

urlpatterns = [
    path('', cache_page(60)(HomeView.as_view()), name='index'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('/clientcreate/', ClientCreateView.as_view(), name='clientcreate'),
    path('/clientupdate/<int:pk>/', ClientUpdateView.as_view(), name='clientupdate'),
    path('/clientdelete/<int:pk>/', ClientDeleteView.as_view(), name='clientdelete'),

    path('message/', MessageListView.as_view(), name='list'),
    path('messagedetail/<int:pk>/', MessageDetailView.as_view(), name='messagedetail'),
    path('messagecreate', MessageCreateView.as_view(), name='messagecreate'),
    path('messageupdate/<int:pk>/', MessageUpdateView.as_view(), name='messageupdate'),
    path('messagedelete/<int:pk>/', MessageDeleteView.as_view(), name='messagedelete'),
    path("/mailblock/<int:pk>/", ActivateMessage, name="block")


]
