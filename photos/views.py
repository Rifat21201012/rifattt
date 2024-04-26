from django.shortcuts import render, redirect
from . import forms
from .models import Photo


# Create your views here.
def add_photo(request):
    if request.method == "POST":
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = forms.PhotoForm()
    return render(request, 'forms.html', {
        "form": form
    })


def update_photo(request, p_id):
    p = Photo.objects.get(pk=p_id)
    if request.method == "POST":
        form = forms.PhotoForm(request.POST, request.FILES or None, instance=p)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = forms.PhotoForm(instance=p)
    return render(request, 'forms.html', {
        "form": form
    })


def delete_photo(request, p_id):
    Photo.objects.get(pk=p_id).delete()
    return redirect('/')
