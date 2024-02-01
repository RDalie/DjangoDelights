from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("ingredients/list/", views.IngredientListView.as_view(), name="ingredient-list"),
    path("menu/list/", views.MenuListView.as_view(), name="menu-list"),
    path("purchase/list/", views.PurchaseListView.as_view(), name="purchase-list"),
    path("stats", views.stats, name="stats"),
    path("menu/add/", views.MenuCreateView.as_view(), name="menu-add"),
    path("reciperequirement/add/", views.RecipeRequirementCreateView.as_view(), name="reciperequirement-add"),
    path("ingredient/add/", views.IngredientCreateView.as_view(), name="ingredient-add"),
    path("purchase/add/", views.PurchaseCreateView.as_view(), name="purchase-add"),
    path("ingredient/<pk>/update/", views.IngredientUpdateView.as_view(), name="ingredient-update"),
    path('<pk>/delete/', views.IngredientDeleteView.as_view(), name="ingredient-delete"),
]
