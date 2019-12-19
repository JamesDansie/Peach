from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from .models import Dish

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'dish_list'

    def get_queryset(self):
        dish_list = Dish.objects.order_by('id')
        # debugging code
        # print(dish_list, type(dish_list), len(dish_list))
        # If there's no existing dishes, make some dishes.
        if(len(dish_list) < 1):
            d1 = Dish(
                title = "Red Curry",
                img = "https://via.placeholder.com/150",
                restaurant_name = "Thai Place",
                price = 8.99,
                description = "Yummy curry!",
                other_text = "more text",
                votes = 0
            )
            d1.save()
            
            d2 = Dish(
                title = "Fish and Chips",
                img = "https://via.placeholder.com/150",
                restaurant_name = "The Fisherman's Wharf",
                price = 10.99,
                description = "Pippin' hot fish and chips!",
                other_text = "Yummy fish and chips!",
                votes = 1
            )
            d2.save()

            d3 = Dish(
                title = "Burger and Beer",
                img = "https://via.placeholder.com/150",
                restaurant_name = "Jimmy's Imaginary Burger Shack",
                price = 15.99,
                description = "It is the. best. burger.     ever.",
                other_text = "might not be the best burger ever",
                votes = 4
            )
            d3.save()

            # laziness wins
            for x in range(4,9):
                d = Dish(
                    title = "Place holder dish " + str(x),
                    img = "https://via.placeholder.com/150",
                    restaurant_name = "Restaurant " + str(x),
                    price = 10.99 + x,
                    description = "Description " + str(x),
                    other_text = "Other text " + str(x),
                    votes = 0
                )
                print(d)
                d.save()

            dish_list = Dish.objects.order_by('id')
        
        return dish_list

class DetailView(generic.DetailView):
    model = Dish
    template_name = 'polls/detail.html'

def vote(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    dish.votes += 1
    dish.save()
    return HttpResponseRedirect('/')
