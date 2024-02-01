from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from .models import Ingredient, RecipeRequirement, Purchase, MenuItem
from django.urls import reverse_lazy
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout  
from django.urls import reverse

# Create your views here.
@login_required 
def index(request):
    return render(request, "inventory/index.html")

# class IngredientCreateView(CreateView):
#     model = Ingredient
#     fields = ["__all__"]

class IngredientListView(LoginRequiredMixin,ListView):
    model = Ingredient
    template_name = "inventory/ingredients_list.html"

class IngredientDeleteView(LoginRequiredMixin,DeleteView):
    model = Ingredient
    success_url =  reverse_lazy("ingredient-list")

class MenuListView(LoginRequiredMixin,ListView):
    model = MenuItem
    template_name = "inventory/menu_list.html"

class MenuCreateView(LoginRequiredMixin,CreateView):
    model = MenuItem
    fields = "__all__"
    template_name = "inventory/add_menu_item.html"
    def get_success_url(self):
        return reverse("menu-list")

class IngredientCreateView(LoginRequiredMixin,CreateView):
    model = Ingredient
    fields = "__all__"
    template_name = "inventory/add_ingredient.html"   
    def get_success_url(self):
        return reverse("ingredient-list")

class RecipeRequirementCreateView(LoginRequiredMixin,CreateView):
    model = RecipeRequirement
    fields = "__all__"
    template_name = "inventory/add_reciperequirement.html" 
    def get_success_url(self):
        return reverse("index")

class PurchaseListView(LoginRequiredMixin,ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"

class PurchaseCreateView(LoginRequiredMixin,CreateView):
    model = Purchase
    fields= "__all__"
    template_name = "inventory/add_purchase.html"
    def get_success_url(self):
        return reverse("purchase-list")

class IngredientUpdateView(LoginRequiredMixin,UpdateView):
    model = Ingredient
    fields=['quantity']
    template_name = "inventory/update_ingredient.html"  
    def get_success_url(self):
        return reverse("ingredient-list")  

@login_required
def stats(request):
    purchase_list = Purchase.objects.all()
    total_purchase = 0
    total_revenue = 0
    for obj in purchase_list:
        total_purchase += obj.menu_item.price * obj.quantity
        reciperequirement = obj.menu_item.reciperequirement_set.all()
        for item in reciperequirement:
            total_revenue += item.ingredient.price_per_unit * obj.quantity * item.quantity

    context = {
        'purchase' : total_purchase,
        'cost' : total_revenue,
        'profit' : total_purchase - total_revenue
    }

    return render(request, "inventory/stats.html", context )

def logout_view(request):
    logout(request)
    return redirect('login')

