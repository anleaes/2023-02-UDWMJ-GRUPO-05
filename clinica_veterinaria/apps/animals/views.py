from django.shortcuts import render, redirect
from animals.models import Animal
from animals.forms import AnimalForm


def index_animal(request):
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
        return redirect('index_animal')
    else:
        form = AnimalForm()
    return render(request, 'animals/create_animal.html', {'form': form})

def update_animal(request, id):
    animal = Animal.objects.get(id = id)
    form = AnimalForm(request.POST or None, instance = animal)
    if form.is_valid():
        form.save()
        return redirect("index_animal")
    return render(request, "animals/update_animal.html", {"form" : form, "animal" : animal})

def delete_animal(request, id):
    animal = Animal.objects.get(id = id)
    if request.method == "POST":
        animal.delete()
        return redirect("index_animal")
    return render(request, "animals/delete_animal.html",{"animal" : animal})
        
