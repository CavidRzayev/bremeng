from django.shortcuts import redirect, render,reverse

def index(request):
    return render(request,"index.html")


def contact(request):
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")