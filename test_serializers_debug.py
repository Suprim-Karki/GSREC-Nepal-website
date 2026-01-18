
import os
import sys
import django

# Add current directory to path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gsrec_project.settings')
django.setup()

from core.serializers import CountrySerializer
print("Serializer imported successfully")
