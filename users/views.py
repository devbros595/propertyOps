from django.shortcuts import render

# Create your views here.


def sign_in_view(request):
    return render(request, "sign_in.html")


def sign_up_view(request):
    return render(request, "sign_up.html")
