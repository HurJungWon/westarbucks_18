import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "westarbucks.settings")
django.setup()

from products.models import Menu, Category, Drink, Image

CSV_PATH_PRODUCTS = 'starbucks_crawling.csv'

category_li = []
categories = Category.objects.all()
for category in categories:
    category_li.append(category.name)

drinks_li = []
drinks = Drink.objects.all()
for drink in drinks:
  drinks_li.append(drink.korean_name)

images_li = []
images = Image.objects.all()
for image in images:
  images_li.append(image.image_url)


menu = Menu.objects.get(name="음료")

with open(CSV_PATH_PRODUCTS) as file:
  data_reader = csv.reader(file)
  next(file)
  for row in data_reader:
    if row[1] not in category_li:
      Category.objects.create(name = row[1], menu_id = menu.id)
      category_li.append(row[1])
    if row[2] not in drinks_li:
      category = Category.objects.get(name=row[1])
      Drink.objects.create(korean_name=row[2], english_name=row[3], description=row[4], category_id=category.id)
      drinks_li.append(row[2])
    if row[5] not in images_li:
      drink = Drink.objects.get(korean_name=row[2])
      Image.objects.create(image_url=row[5], drink_id=drink.id)
    
    

