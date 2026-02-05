from django.contrib import admin
from .models import HeroSection, Country, Institution, Service, TestPrep, Testimonial, Resource, Partner, Milestone, Feature, Stat, SiteSettings, AboutUs, LegalPage, ContactPage, HomePageSettings, JourneyStep, ListingPageSettings, BranchOffice

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name',)
    fieldsets = (
        ('General Settings', {
            'fields': ('site_name', 'logo', 'footer_logo', 'favicon', 'footer_description')
        }),
        ('Contact Information', {
            'fields': ('address', 'address_link', 'phone', 'email')
        }),
        ('Social Media Links', {
            'fields': ('facebook_link', 'twitter_link', 'instagram_link', 'linkedin_link', 'youtube_link', 'tiktok_link')
        }),
        ('Footer Headings', {
            'fields': ('footer_company_title', 'footer_destinations_title', 'footer_contact_title')
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'mission_title')
    def has_add_permission(self, request):
        # Allow only one instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title_part1', 'title_part2', 'is_active')

class InstitutionInline(admin.TabularInline):
    model = Institution
    extra = 1

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    inlines = [InstitutionInline]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(TestPrep)
class TestPrepAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'order')
    list_editable = ('order',)

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_type', 'size_label')

@admin.register(LegalPage)
class LegalPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('year', 'title')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('number', 'label', 'order')

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(HomePageSettings)
class HomePageSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(JourneyStep)
class JourneyStepAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

@admin.register(ListingPageSettings)
class ListingPageSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(BranchOffice)
class BranchOfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'order')
