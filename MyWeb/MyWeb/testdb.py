from TestModel.models import Test,Phones
from django.http import HttpResponse
from django.shortcuts import render
import chardet

def showPhone(request):
    phone_list=Phones.objects.all()
    return render(request, 'ShowPhone.html', {'phone_list': phone_list})
    

def showDB(request):
    movie_list = Test.objects.all()

    return render(request, 'ShowMovies.html', {'movie_list': movie_list})    