from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('study/<slug:slug>/', views.destination_detail, name='destination_detail'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    
    # New Pages
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('downloads/', views.downloads, name='downloads'),
    path('success-stories/', views.success_stories, name='success_stories'),
    
    # List Views (for "View All")
    path('study/', views.destination_list, name='destination_list'),
    path('services/', views.service_list, name='service_list'),
    
    # Test Prep
    path('test-prep/', views.test_prep_list, name='test_prep_list'),
    path('test-prep/<slug:slug>/', views.test_prep_detail, name='test_prep_detail'),
]
