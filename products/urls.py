from django.urls import path

from products.views import CategoryView
from products.views import DrinkView
from products.views import AllDrinkView


urlpatterns = [
  path('/category', CategoryView.as_view()),
  path('/drink', DrinkView.as_view()),
  path('/alldrink', AllDrinkView.as_view())
]
