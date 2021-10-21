from django.db import models
from django.shortcuts import redirect, render
from myapp.models import Photo, Category

# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    if category is None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
        
    categories = Category.objects.all()
    return render(request, 'gallery.html', {'categories':categories, 'photos':photos})


def addPhoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES['image']
        if data['cat'] != None:
            category, created = Category.objects.get_or_create(name=data['cat'])
        else:
            category = Category.objects.get(id=data['category'])
        photo = Photo.objects.create(
            category=category,
            image=image,
            desc=data['desc']
        )
        photo.save()
        return redirect('gallery')
    return render(request, 'add.html', {'categories':categories})


def viewPhoto(request, pk):
    return render(request, 'photo.html')
