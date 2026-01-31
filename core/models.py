from django.db import models
from django.utils.text import slugify

# Singleton Model for Hero Section (simplified as just a model, could use specific package but simple is fine)
class HeroSection(models.Model):
    title_part1 = models.CharField(max_length=100, default="Dream Big.")
    title_part2 = models.CharField(max_length=100, default="Study Global.")
    subtitle = models.TextField()
    background_image = models.ImageField(upload_to='hero/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Hero: {self.title_part1} {self.title_part2}"

    class Meta:
        verbose_name_plural = "Hero Section"

class Feature(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="FontAwesome class e.g. fa-file-circle-check")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class Stat(models.Model):
    number = models.CharField(max_length=20, help_text="e.g. 12+, 5k+")
    label = models.CharField(max_length=50, help_text="e.g. Years Experience")
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.number} {self.label}"

    class Meta:
        ordering = ['order']

class Country(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=100)
    flag_emoji = models.CharField(max_length=10, blank=True, null=True, help_text="Emoji flag or similar")
    background_image = models.ImageField(upload_to='countries/', blank=True, null=True)
    intro = models.TextField()
    facts = models.JSONField(default=list, help_text="List of facts")
    universities = models.JSONField(default=list, help_text="List of top universities")
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['order', 'name']

class Service(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=50, help_text="FontAwesome class e.g., fa-compass")
    intro = models.TextField()
    features = models.JSONField(default=list, help_text="List of features")
    process = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']

class TestPrep(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=50, help_text="Short name e.g., IELTS")
    full_name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=50)
    intro = models.TextField()
    format_data = models.JSONField(default=list, help_text="List of format sections")
    score_scale = models.CharField(max_length=100)
    validity = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.university}"

class Resource(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='resources/')
    file_type = models.CharField(max_length=10, help_text="PDF, DOCX etc.")
    icon_class = models.CharField(max_length=50, default="fa-file-arrow-down")
    size_label = models.CharField(max_length=20, help_text="e.g. 4.5 MB")

    def __str__(self):
        return self.title

class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Milestone(models.Model):
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.year}: {self.title}"

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="GSREC NEPAL")
    logo = models.ImageField(upload_to='site/', blank=True, null=True, help_text="Main logo for Header")
    footer_logo = models.ImageField(upload_to='site/', blank=True, null=True, help_text="Logo for Footer. Defaults to main logo if not set.")
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    
    # Footer Content
    footer_description = models.TextField(blank=True, default="Global Student Research & Educational Consultancy (GSREC Nepal) is a leading educational consultancy in Nepal, dedicated to providing ethical and reliable counseling services to students.")
    
    # Contact Info
    address = models.CharField(max_length=200, default="New Baneshwor, Kathmandu, Nepal")
    phone = models.CharField(max_length=50, default="+977 1-4244XXX")
    email = models.EmailField(default="info@gsrecnepal.com")
    
    # Social Media
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            # If you want to ensure only one instance exists, you can handle it here, 
            # or just rely on using .first() in views/context.
            pass
        super().save(*args, **kwargs)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Site Settings"

class AboutUs(models.Model):
    # Main Section
    title = models.CharField(max_length=100, default="About GSREC Nepal")
    subtitle = models.CharField(max_length=200, default="Global Student Recruitment & Education Consultancy (GSREC)")
    main_image = models.ImageField(upload_to='about/', blank=True, null=True, help_text="Main image for About Us page")

    # Mission Section
    mission_title = models.CharField(max_length=100, default="Our Mission")
    mission_description = models.TextField(default="At GSREC Nepal, based in Putalisadak, Kathmandu, we are committed to providing genuine and professional guidance to students aspiring to study abroad.")

    # Stats
    stat1_number = models.CharField(max_length=20, default="5000+", help_text="e.g. 5000+")
    stat1_label = models.CharField(max_length=50, default="Students Placed")
    
    stat2_number = models.CharField(max_length=20, default="98%", help_text="e.g. 98%")
    stat2_label = models.CharField(max_length=50, default="Visa Success Rate")

    def save(self, *args, **kwargs):
        if not self.pk and AboutUs.objects.exists():
            pass # Singleton logic
        super().save(*args, **kwargs)

    def __str__(self):
        return "About Us Page Content"

    class Meta:
        verbose_name_plural = "About Us Page"

class LegalPage(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField(help_text="Content for the page (HTML supported)")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
