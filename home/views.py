from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def banner(request):
    return render(request,'banner.html')

def contact(request):
    return render(request,'contact.html')

def demo(request):
    return render(request,'demo.html')

def faq(request):
    return render(request,'faq.html')

def footer(request):
    return render(request,'footer.html')

def form(request):
    return render(request,'form.html')

def hero(request):
    return render(request,'hero.html')

def payment(request):
    return render(request,'payment.html')

def registerform(request):
    return render(request,'registerform.html')

def reviews(request):
    return render(request,'reviews.html')

def searchResults(request):
    return render(request,'searchResults.html')

def service(request):
    return render(request,'service.html')

def service1(request):
    return render(request,'service1.html')