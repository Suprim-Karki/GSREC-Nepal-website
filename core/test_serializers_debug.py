
import os
import django
from django.conf import settings

# Setup Django environment
import sys
sys.path.append('..') # Add gsrec/ to path so we can import gsrec.settings if needed, or just relying on manage.py context?
# Actually simpler to set DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gsrec.settings')
django.setup()

from core.serializers import CountrySerializer, ServiceSerializer
from core.models import Country, Service

print("Import successful")
try:
    s = CountrySerializer()
    print("CountrySerializer initialized")
except Exception as e:
    print(f"Error initializing CountrySerializer: {e}")
