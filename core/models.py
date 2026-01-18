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

class Download(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='downloads/')
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
