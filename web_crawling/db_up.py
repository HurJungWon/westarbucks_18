from products.models import Menu, Category, Drink, Images
import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "westarbucks.settings")
django.setup()
