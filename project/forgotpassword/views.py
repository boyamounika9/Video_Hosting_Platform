from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages

def forgot_password(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        new_password = request.POST.get('new_password')

        try:

            user = User.objects.get(username=username)

            user.set_password(new_password)

            user.save()

            messages.success(request,'Password changed successfully')

            return redirect('login')

        except User.DoesNotExist:

            messages.error(request,'User not found')

    return render(request,'forgot_password.html')