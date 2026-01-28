from .models import Country, Service, TestPrep, SiteSettings, Partner

def global_context(request):
    return {
        'global_countries': Country.objects.all(),
        'global_services': Service.objects.all(),
        'global_test_preps': TestPrep.objects.all(),
        'site_settings': SiteSettings.objects.first(),
        'partners': Partner.objects.all(),
    }
