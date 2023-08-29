from django.views.decorators.cache import cache_page
from django.urls import path
from blog.views import *
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('create/', MaterialsCreateView.as_view(), name='create'),
    path('', cache_page(60)(MaterialsListView.as_view()), name='list'),
    path('view/<int:pk>', MaterialsDetailView.as_view(), name='view'),
    path('edit/<int:pk>', MaterialsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', MaterialsDeleteView.as_view(), name='delete'),

]
