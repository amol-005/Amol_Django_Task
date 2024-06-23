from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard/", dashboard_view, name='dashboard'),
    path("add/", add_view, name='add'),
    path("edit/<int:id>/", update_view, name='edit'),
    path("delete/<int:id>/", delete_view, name='delete'),
    path("save_edit/", save_view, name='save_edit'),
]
