from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('arts/', views.arts_index, name='index'),
  path('arts/<int:art_id>/', views.arts_detail, name='detail'),
  path('arts/create/', views.ArtCreate.as_view(), name='arts_create'),
  path('arts/<int:pk>/update/', views.ArtUpdate.as_view(), name='arts_update'),
  path('arts/<int:pk>/delete/', views.ArtDelete.as_view(), name='arts_delete'),
  path('arts/<int:art_id>/add_display/', views.add_display, name='add_display'),
  path('arts/<int:art_id>/assoc_museum/<int:museum_id>/', views.assoc_museum, name='assoc_museum'),
  path('arts/<int:art_id>/unassoc_museum/<int:museum_id>/', views.unassoc_museum, name='unassoc_museum'),
  path('museums/', views.MuseumList.as_view(), name='museums_index'),
  path('museums/<int:pk>/', views.MuseumDetail.as_view(), name='museums_detail'),
  path('museums/create/', views.MuseumCreate.as_view(), name='museums_create'),
  path('museums/<int:pk>/update/', views.MuseumUpdate.as_view(), name='museums_update'),
  path('museums/<int:pk>/delete/', views.MuseumDelete.as_view(), name='museums_delete'),
]