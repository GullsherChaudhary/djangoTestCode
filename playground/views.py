from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
#it a request handler file or action file

def say_hello(request):
    #fetch data from db

    return HttpRequest('Helloword!')

def sayHelloViaHtml(request):
    return render(request, 'hello.html')

def renderHtmlwithDynamicValue(request):
    return render(request, 'hello.html', {'name':'YourName'})