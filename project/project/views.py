from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def playback(request):
    return render(request,"playback.html")

def profile(request):
    return render(request,"profile.html")

def register(request):
    return render(request,"register.html")

def upload(request):
    return render(request,"upload.html")