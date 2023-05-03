from django.shortcuts import render
from .models import Library


def index(request):

    # imports all the photos and save it in the database

    photo = Library.objects.all()

    cloudinary_img = {'photo': photo}

    return render(request, 'index.html', cloudinary_img)
