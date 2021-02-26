from django.db import models


class Menu(models.Model):
  name = models.CharField(max_length=20)

  class Meta:
    db_table = 'menus'

class Category(models.Model):
  name = models.CharField(max_length=45)
  menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

  class Meta:
    db_table = 'categories'

class Drink(models.Model):
  korean_name  = models.CharField(max_length=45)
  english_name = models.CharField(max_length=45)
  description  = models.TextField()
  category     = models.ForeignKey(Category, on_delete=models.CASCADE)

  class Meta:
    db_table = 'drinks'

class Image(models.Model):
  image_url = models.CharField(max_length=2000)
  drink     = models.ForeignKey(Drink, on_delete=models.CASCADE)

  class Meta:
    db_table = 'images'

class Nutrition(models.Model):
  one_serving_kca  = models.DecimalField(max_digits=6, decimal_places=2, null=True)
  sodium_mg        = models.DecimalField(max_digits=6, decimal_places=2, null=True)
  saturated_fat_g  = models.DecimalField(max_digits=6, decimal_places=2, null=True)
  sugars_g         = models.DecimalField(max_digits=6, decimal_places=2, null=True)
  protein_g        = models.DecimalField(max_digits=6, decimal_places=2, null=True)
  caffeine_mg      = models.DecimalField(max_digits=6, decimal_places=2, null=True)
  size_ml          = models.CharField(max_length=45)
  size_fluid_ounce = models.CharField(max_length=45)
  drink            = models.ForeignKey(Drink, on_delete=models.CASCADE)

  class Meta:
    db_table = 'nutritions'

class Allergy(models.Model):
  name = models.CharField(max_length=45)

  class Meta:
    db_table = 'allergy'

class AllergyDrink(models.Model):
  allergy  = models.ForeignKey(Allergy, on_delete=models.CASCADE)
  drink    = models.ForeignKey(Drink, on_delete=models.CASCADE)

  class Meta:
    db_table = 'allergy_drinks'



