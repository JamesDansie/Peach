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
        return Dish.objects.order_by('id')

# def index(request):
#     dish_list = Dish.objects.order_by('id')
#     context = {
#         'dish_list': dish_list,
#     }
#     return render(request, 'polls/index.html', context)

#     # #Original version
#     # template = loader.get_template('polls/index.html')
#     # return HttpResponse(template.render(context, request))

class DetailView(generic.DeleteView):
    model = Dish
    template_name = 'polls/detail.html'

# def detail(request, dish_id):
#     dish = get_object_or_404(Dish, pk=dish_id)
#     return render(request, 'polls/detail.html', {'dish': dish})

# need to figure out how to save an image
# if it is handled on the server side it will be here
# if is is handled with client side js, then this is not needed.
def image(request, dish_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % dish_id)

def vote(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    dish.votes += 1
    dish.save()
    return HttpResponseRedirect('/')
