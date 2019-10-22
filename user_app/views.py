from django.db.models import Q
from django.shortcuts import render, redirect
from user_app.models import UserInfo
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        sex = request.POST.get("sex")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        birthday = request.POST.get("birthday")
        UserInfo.objects.create(
            username=username,
            password=make_password(password),
            sex=sex,
            email=email,
            phone=phone,
            birthday=birthday
        )
        return redirect("/login/")

    return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password").strip()
        user_objs = UserInfo.objects.filter(Q(username=username) | Q(email=username) | Q(phone=username))
        if user_objs and check_password(password, user_objs[0].password):
            return render(request, "index.html")
    return render(request, "login.html")
