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
    path('test-prep/<slug:slug>/register/', views.test_prep_register, name='test_prep_register'),
    
    # API Endpoints
    path('api/countries/', views.CountryListAPIView.as_view(), name='country-list-api'),
    path('api/services/', views.ServiceListAPIView.as_view(), name='service-list-api'),
    path('api/test-preps/', views.TestPrepListAPIView.as_view(), name='test-prep-list-api'),
    path('api/features/', views.FeatureListAPIView.as_view(), name='feature-list-api'),
    path('api/stats/', views.StatListAPIView.as_view(), name='stat-list-api'),
    path('api/home-data/', views.home_data, name='home-data-api'),
]
