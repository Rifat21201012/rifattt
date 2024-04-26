from django.shortcuts import render
from products.models import Product
from photos.models import Photo

def home(request):
    products = Product.objects.all()
    photos = Photo.objects.all()
    return render(request, 'home.html', {
        "products": products,
        "photos": photos,
    })
