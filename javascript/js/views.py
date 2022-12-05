from django.shortcuts import render

# Create your views here.

def element(request):
    return render(request,'js_prgm/element.html')

def element_find(request):
    return render(request,'js_prgm/element_find.html')

def largest(request):
    return render(request,'js_prgm/largest.html')

def second_largest(request):
    return render(request,'js_prgm/second_largest.html')

def palindrome(request):
    return render(request,'js_prgm/palindrome.html')
