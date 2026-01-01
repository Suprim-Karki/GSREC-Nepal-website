from django.shortcuts import render, get_object_or_404
from .models import HeroSection, Country, Service, TestPrep, Testimonial, Download, Partner, Milestone, Feature, Stat

def index(request):
    hero = HeroSection.objects.filter(is_active=True).first()
    countries = Country.objects.all()
    services = Service.objects.all()
    test_preps = TestPrep.objects.all()
    testimonials = Testimonial.objects.all()
    partners = Partner.objects.all()
    features = Feature.objects.all()
    stats = Stat.objects.all()
    
    context = {
        'hero': hero,
        'countries': countries,
        'services': services,
        'test_preps': test_preps,
        'testimonials': testimonials,
        'partners': partners,
        'features': features,
        'stats': stats,
    }
    return render(request, 'core/home.html', context)

def about(request):
    milestones = Milestone.objects.all().order_by('year')
    partners = Partner.objects.all()
    context = {
        'milestones': milestones,
        'partners': partners
    }
    return render(request, 'core/about.html', context)

def contact(request):
    if request.method == 'POST':
        # Handle form submission logic here (e.g. send email or save to DB)
        return render(request, 'core/contact.html', {'submitted': True})
    return render(request, 'core/contact.html')

def downloads(request):
    downloads_list = Download.objects.all()
    return render(request, 'core/downloads.html', {'downloads': downloads_list})

def success_stories(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'core/success_stories.html', {'testimonials': testimonials})

# Destinations
def destination_list(request):
    countries = Country.objects.all()
    return render(request, 'core/destination_list.html', {'countries': countries})

def destination_detail(request, slug):
    country = get_object_or_404(Country, slug=slug)
    countries = Country.objects.all()
    test_preps = TestPrep.objects.all()
    services = Service.objects.all()
    context = {
        'country': country, 
        'countries': countries, 
        'services': services, 
        'test_preps': test_preps
    }
    return render(request, 'core/destination_detail.html', context)

# Services
def service_list(request):
    services = Service.objects.all()
    return render(request, 'core/service_list.html', {'services': services})

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
    return render(request, 'core/test_prep_list.html', {'test_preps': test_preps})

def test_prep_detail(request, slug):
    test_prep = get_object_or_404(TestPrep, slug=slug)
    # Context for menu
    countries = Country.objects.all()
    services = Service.objects.all()
    test_preps = TestPrep.objects.all()
    
    context = {
        'test_prep': test_prep,
        'countries': countries, 
        'services': services, 
        'test_preps': test_preps
    }
    return render(request, 'core/test_prep_detail.html', context)
