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
        category = request.POST['category']
        desc = request.POST['desc']
        image = request.FILES['image']
        photo = Photo.objects.create(
            category=Category.objects.get(id=category),
            image=image,
            desc=desc
        )
        photo.save()
        return redirect('gallery')
    return render(request, 'add.html', {'categories':categories})


def viewPhoto(request, pk):
    return render(request, 'photo.html')
