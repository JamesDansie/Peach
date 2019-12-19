from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # generic views (classes) us pk, functions use id's
    # ex: /
    path('', views.IndexView.as_view(), name='index'),
    # ex: /5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /5/image/
    path('<int:dish_id>/image/', views.image, name='image'),
    # ex: /5/vote/
    path('<int:dish_id>/vote/', views.vote, name='vote'),
]
