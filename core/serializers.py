from rest_framework import serializers
from .models import Country, Service, TestPrep, Feature, Stat, HeroSection, Testimonial, Download, Partner, Milestone

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class TestPrepSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPrep
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = '__all__'

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'