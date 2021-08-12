from django.shortcuts import render, redirect
from .forms import Email_senderForm
from .models import Email_sender
# Create your views here.


def index(request):
    form =  Email_senderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile/')
    return render(request, 'index.html',{"form": form})

def profile(request):
    info = Email_sender.objects.all()
    return render(request,'email.html',{"info": info})
      
