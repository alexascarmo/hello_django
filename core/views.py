from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos<h1>'.format(nome, idade))

def soma(request, num1, num2):
    total = num1 + num2
    return HttpResponse('A soma do numero {} com o numero {} é igual a {}'.format(num1, num2, total))