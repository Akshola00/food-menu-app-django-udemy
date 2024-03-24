from django.urls import path
from . import views
# app_name = 'food' name spacnig for where there are two or more apps with same url name
urlpatterns=[
    path('', views.index, name='index' ),
    path('item/', views.item, name='item' ),
    path('<int:item_id>', views.detail, name='details'),

    # add view
    path('add', views.create_item, name='create_item'),
    path('update/<int:id>/', views.update_food, name='update_food'),
    path('delete/<int:id>/', views.delete, name='delete'),
]