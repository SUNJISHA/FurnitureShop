from django.shortcuts import render

# Create your views here.


def exam_home(request):
    return render(request,'exam/home.html')

def exam_login(request):
    return render(request,'exam/login.html')

def exam_about(request):
    return render(request,'exam/about.html')

def exam_reg(request):
    return render(request,'exam/reg.html')

def exam_shop(request):
    return render(request,'exam/shop.html')

def exam_cart(request):
    return render(request,'exam/cart.html')