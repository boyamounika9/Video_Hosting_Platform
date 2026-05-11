from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):

    current_user = request.user

    return render(request,'profile.html',{
        'user_data':current_user
    })