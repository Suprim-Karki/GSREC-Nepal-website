from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HeroSection, Country, Service, TestPrep, Testimonial, Resource, Partner, Milestone, Feature, Stat, AboutUs, LegalPage, ContactPage, HomePageSettings, JourneyStep, ListingPageSettings, BranchOffice
from .serializers import (
    CountrySerializer, ServiceSerializer, TestPrepSerializer, FeatureSerializer, StatSerializer,
    HeroSectionSerializer, TestimonialSerializer, ResourceSerializer, PartnerSerializer, MilestoneSerializer
)

def index(request):
    hero = HeroSection.objects.filter(is_active=True).first()
    countries = Country.objects.all()
    services = Service.objects.all()
    test_preps = TestPrep.objects.all()
    testimonials = Testimonial.objects.all()
    partners = Partner.objects.all()
    features = Feature.objects.all()
    stats = Stat.objects.all()
    
    home_settings = HomePageSettings.objects.first()
    journey_steps = JourneyStep.objects.all()
    
    context = {
        'hero': hero,
        'countries': countries,
        'services': services,
        'test_preps': test_preps,
        'testimonials': testimonials,
        'partners': partners,
        'features': features,
        'stats': stats,
        'home_settings': home_settings,
        'journey_steps': journey_steps,
    }
    return render(request, 'core/home.html', context)

def about(request):
    milestones = Milestone.objects.all().order_by('year')
    partners = Partner.objects.all()
    about_us = AboutUs.objects.first()
    branch_offices = BranchOffice.objects.all()
    context = {
        'milestones': milestones,
        'partners': partners,
        'about': about_us,
        'branch_offices': branch_offices,
    }
    return render(request, 'core/about.html', context)

def contact(request):
    contact_page = ContactPage.objects.first()
    submitted = False
    if request.method == 'POST':
        # Handle form submission logic here (e.g. send email or save to DB)
        submitted = True
    
    # Context for form
    global_test_preps = TestPrep.objects.all()
    
    return render(request, 'core/contact.html', {
        'submitted': submitted, 
        'contact_page': contact_page,
        'global_test_preps': global_test_preps
    })

def resources(request):
    resources_list = Resource.objects.all()
    listing_settings = ListingPageSettings.objects.first()
    return render(request, 'core/resources.html', {'resources': resources_list, 'listing_settings': listing_settings})

def legal_page_detail(request, slug):
    page = get_object_or_404(LegalPage, slug=slug)
    return render(request, 'core/legal_page.html', {'page': page})

def success_stories(request):
    testimonials = Testimonial.objects.all()
    listing_settings = ListingPageSettings.objects.first()
    return render(request, 'core/success_stories.html', {'testimonials': testimonials, 'listing_settings': listing_settings})

# Destinations
def destination_list(request):
    countries = Country.objects.all()
    listing_settings = ListingPageSettings.objects.first()
    return render(request, 'core/destination_list.html', {'countries': countries, 'listing_settings': listing_settings})

def destination_detail(request, slug):
    country = get_object_or_404(Country, slug=slug)
    countries = Country.objects.all()
    test_preps = TestPrep.objects.all()
    services = Service.objects.all()
    
    submitted = False
    if request.method == 'POST':
        submitted = True
        
    context = {
        'country': country, 
        'countries': countries, 
        'services': services, 
        'test_preps': test_preps,
        'global_test_preps': test_preps, # For partial
        'submitted': submitted
    }
    return render(request, 'core/destination_detail.html', context)

# Services
def service_list(request):
    services = Service.objects.all()
    listing_settings = ListingPageSettings.objects.first()
    return render(request, 'core/service_list.html', {'services': services, 'listing_settings': listing_settings})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    countries = Country.objects.all()
    services = Service.objects.all()
    test_preps = TestPrep.objects.all() 
    context = {
        'service': service, 
        'countries': countries, 
        'services': services, 
        'test_preps': test_preps
    }
    return render(request, 'core/service_detail.html', context)

# Test Prep
def test_prep_list(request):
    test_preps = TestPrep.objects.all()
    listing_settings = ListingPageSettings.objects.first()
    return render(request, 'core/test_prep_list.html', {'test_preps': test_preps, 'listing_settings': listing_settings})

def test_prep_detail(request, slug):
    test_prep = get_object_or_404(TestPrep, slug=slug)
    # Context for menu
    countries = Country.objects.all()
    services = Service.objects.all()
    test_preps = TestPrep.objects.all()
    
    submitted = False
    if request.method == 'POST':
        submitted = True
    
    context = {
        'test_prep': test_prep,
        'countries': countries, 
        'services': services, 
        'test_preps': test_preps,
        'global_test_preps': test_preps, # For partial
        'submitted': submitted
    }
    return render(request, 'core/test_prep_detail.html', context)

def test_prep_register(request, slug):
    test_prep = get_object_or_404(TestPrep, slug=slug)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        preferred_time = request.POST.get('preferred_time')
        message = request.POST.get('message')
        
        # Here you could save to database, send email, etc.
        # For now, we'll just redirect with success message
        from django.contrib import messages
        messages.success(request, f'Thank you {name}! We have received your registration for {test_prep.name}. Our team will contact you soon.')
        
        return redirect('test_prep_detail', slug=slug)
    
    # If GET request, redirect to detail page
    return redirect('test_prep_detail', slug=slug)

# API Views
class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all().order_by('order', 'name')
    serializer_class = CountrySerializer

class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.all().order_by('order', 'title')
    serializer_class = ServiceSerializer

class TestPrepListAPIView(generics.ListAPIView):
    queryset = TestPrep.objects.all().order_by('order', 'name')
    serializer_class = TestPrepSerializer

class FeatureListAPIView(generics.ListAPIView):
    queryset = Feature.objects.all().order_by('order')
    serializer_class = FeatureSerializer

class StatListAPIView(generics.ListAPIView):
    queryset = Stat.objects.all().order_by('order')
    serializer_class = StatSerializer

@api_view(['GET'])
def home_data(request):
    hero = HeroSection.objects.filter(is_active=True).first()
    countries = Country.objects.all().order_by('order', 'name')
    services = Service.objects.all().order_by('order', 'title')
    test_preps = TestPrep.objects.all().order_by('order', 'name')
    testimonials = Testimonial.objects.all()
    partners = Partner.objects.all()
    features = Feature.objects.all().order_by('order')
    stats = Stat.objects.all().order_by('order')
    
    data = {
        'hero': HeroSectionSerializer(hero).data if hero else None,
        'countries': CountrySerializer(countries, many=True).data,
        'services': ServiceSerializer(services, many=True).data,
        'test_preps': TestPrepSerializer(test_preps, many=True).data,
        'testimonials': TestimonialSerializer(testimonials, many=True).data,
        'partners': PartnerSerializer(partners, many=True).data,
        'features': FeatureSerializer(features, many=True).data,
        'stats': StatSerializer(stats, many=True).data,
    }
    return Response(data)
