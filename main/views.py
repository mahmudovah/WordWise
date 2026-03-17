from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpRequest
from main.models import User

def login_view(request: HttpRequest):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if not user:
            messages.error(request, "E-mail yoki parol xato!")
            return redirect("login")

        login(request, user)
        messages.success(request, "Tizimga muvaffaqqiyatli kirdingiz!")
        return redirect("login")
    return render(request, "auth/login.html")

def register_view(request: HttpRequest):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Bunday email mavjud")
            return redirect("register")

        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        messages.success(request, "Ro'yxatdan o'tdingiz")
        return redirect("login")

    return render(request, 'auth/register.html')

