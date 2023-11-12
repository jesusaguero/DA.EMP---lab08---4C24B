from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('producto',views.SeriesView.as_view(),name='producto'),
    path('producto/<int:producto_id>',views.SerieDetailView.as_view())
]
