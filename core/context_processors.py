from .models import Country, Service, TestPrep

def global_context(request):
    return {
        'global_countries': Country.objects.all(),
        'global_services': Service.objects.all(),
        'global_test_preps': TestPrep.objects.all(),
    }
