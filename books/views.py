from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


# Create your views here.
@csrf_exempt
def books(request):
    if request.method == "GET":
        books=Book.objects.all().values()
        return JsonResponse({"books":list(books)})
    elif request.method=="POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        price=request.POST.get('price')
        inventory=request.POST.get('inventory')
        book=Book(title=title,author=author,price=price,inventory=inventory)
        try:
            book.save()
            return JsonResponse(model_to_dict(books),status=201)
        except IntegrityError as e:
            return JsonResponse({"error":"true","message":"Required field missing"},status=400)

