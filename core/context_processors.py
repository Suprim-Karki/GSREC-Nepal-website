from .models import Country, Service, TestPrep

def global_context(request):
    """
    Make common data available to all templates (for Navbar dropdowns).
    """
    return {
        'global_countries': Country.objects.all().order_by('order'),
        'global_services': Service.objects.all().order_by('order'),
        'global_test_preps': TestPrep.objects.all().order_by('order'),
    }
