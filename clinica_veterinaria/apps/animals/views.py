from django.shortcuts import render, redirect
from animals.models import Animal
from animals.forms import AnimalForm


def index(request):
    animals = Animal.objects.all()
    context = {"animals" : animals}
    return render(request, "animals/list_animals.html", context)

def create_animal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        weight = request.POST.get('weight')
        animal = Animal(name=name, age=age, weight=weight)
        animal.save()
        return redirect('index')
    else:
        form = AnimalForm()
    return render(request, 'animals/create_animal.html', {'form': form})
