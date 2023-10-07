import json
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login , logout
from itertools import chain
# Create your views here.

def signup(request):
     if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
           user = form.save()
           login(request,user)
           return redirect(reverse(index))
     else:
       form = UserCreationForm() 
     return render (request, 'page/signup.html',{'form':form})
 
def index (request):
     return render(request,'page/index.html')

def login_view(request):
     if request.method == 'POST':
          form = AuthenticationForm(data=request.POST)
          if form.is_valid():
           user = form.get_user()
           login(request,user)
           return redirect(reverse(index))
     else:
       form = AuthenticationForm() 
     return render (request, 'page/login.html',{'form':form})
   
    
     return render(request,'page/login.html')

def logout_view(request):
     if request.method == 'POST':
          logout(request)
     return redirect(reverse(index))



def collection (request):
     search = Book.objects.all()
     
     title = None
     author = None
     if 'search_name'in request.GET:
          title = request.GET['search_name']
          if title:
               search = search.filter(title__icontains = title)
                         

          

         
     context = {
          'category': category.objects.all(),
          'book' : search,

     }


     return render(request,'page/Collection.html', context) 


def information (request):
     return render(request,'page/Information.html') 
 
    
def profile (request):
     return render(request,'page/profile.html') 
    