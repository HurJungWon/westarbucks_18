import json

from django.views import View 
from django.http  import JsonResponse

from .models import Drink
from .models import Category
from .models import Menu

class CategoryView(View):
  def get(self, request):
    
    categories = Category.objects.all()
    
    result = []
    
    for category in categories:
      my_dict = {
        'name'     : category.name,
        'id'       : category.id,
        'menu_name': category.menu.name
      }
      result.append(my_dict)

    return JsonResponse({'result': result}, status=200)

  def post(self, request):
    data = json.loads(request.body)
    menu_id = Menu.objects.get(name=data['menu_name']).id
    Category.objects.create(name=data['name'], menu_id=menu_id)

    return JsonResponse({'result': 'SUCCESS'}, status=200)

class DrinkView(View):
  def get(self, request):
      drinks = Drink.objects.all()
      result = []
      
      for drink in drinks:
        my_dict = {
          'korean_name'  : drink.korean_name,
          'english_name' : drink.english_name,
          'description'  : drink.description,
          'category_name': drink.category.name,
        }
        result.append(my_dict)

      return JsonResponse({'result': result}, status=200)

  def post(self, request):
    data = json.loads(request.body)
    category_id = Category.objects.get(name=data['category_name']).id
    kor_name = data['korean_name']
    en_name = data['english_name']
    

    Drink.objects.create(korean_name=kor_name, english_name=en_name, description=data['description'], category_id=category_id)

    return JsonResponse({'result': 'SUCCESS'}, status=200)

class AllDrinkView(View):
  def get(self, request):
    data = json.loads(request.body)

    category = Category.objects.get(name=data['name'])
    drinks = category.drink_set.all()
    print(drinks)
    result = []
    
    for drink in drinks:
      my_dict = {
        'korean_name' : drink.korean_name,
        'english_name': drink.english_name,
        'description' : drink.description,
      }
      result.append(my_dict)
    
    return JsonResponse({'result': result}, status=200)



  






# class ProductView(View):
#   def get(self, request):
#     products = Drink.objects.all()

#     result = []
#     for product in products:
#       my_dict = {
#         'name'       : product.korean_name,
#         'description': product.description
#       }
#       result.append(my_dict)
    

#     return JsonResponse({'result': result}, status=200)

#   def post(self, request):
#     data   = json.loads(request.body)
#     k_name = data['korean_name']
#     e_name = data['english_name']
#     des    = data['description']
#     cat    = data['category_id']

#     Drink.objects.create(korean_name=k_name, english_name=e_name, description=des, category_id=cat)

#     return JsonResponse({'message' : 'SUCC'}, status=200)
    


