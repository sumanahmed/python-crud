from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact_page'),
    path('crud-list', views.list, name='contact_crud_list'),
    path('crud-create', views.create, name='contact_crud_create'),
    path('crud-store', views.store, name='contact_crud_store'),
    path('crud-edit/<int:id>', views.edit, name='contact_crud_edit'),
    path('crud-update/<int:id>', views.update, name='contact_crud_edit'),
    path('crud-destroy/<int:id>', views.destroy, name='contact_crud_edit'),
]
