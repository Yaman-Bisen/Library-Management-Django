from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from .forms import AddBook
from django.contrib import messages
import requests
import json

from .forms import LoginForm, RegisterForm

# Create your views here.


def home(request):
    return render(request, 'app/home.html')

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'app/login.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('login')

@login_required
def adminDashboard(request):
    if request.user.is_authenticated:
        return render(request, 'app/admindashboard.html')
    else:
        return HttpResponseRedirect('/login/')

@login_required
def viewBooks(request):
    email = request.user.email
    headers = {'Content-type': 'application/json'}
  
    r = requests.get(f'http://127.0.0.1:8000/bookinfo/{email}/', headers=headers)

    data = r.json()
    
    return render(request, 'app/viewBooks.html', {'data':data})

@login_required
def addBook(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddBook(request.POST)
            if form.is_valid():
                bname = form.cleaned_data['book_name']
                aname = form.cleaned_data['author_name']
                quan = form.cleaned_data['quantity']
                email = request.user.email

                data = {
                    'user':email,
                    'book_name':bname,
                    'author_name':aname,
                    'quantity':quan,
                }

                headers = {'Content-type': 'application/json'}
                json_data = json.dumps(data)

                r = requests.post('http://127.0.0.1:8000/api/crud/', data=json_data, headers=headers)

                msg = r.json()

                if(r.status_code == 201):
                    messages.success(request,'Book added successfully !!!')
                else:
                    messages.error(request,'Something went wronge !!!')
                form = AddBook()
        else:
            form = AddBook()
        return render(request, 'app/addBook.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

@login_required
def updateBook(request):
    email = request.user.email
    headers = {'Content-type': 'application/json'}
  
    r = requests.get(f'http://127.0.0.1:8000/bookinfo/{email}/', headers=headers)

    data = r.json()
    return render(request, 'app/updateBook.html', {'data':data})

@login_required
def updateBookDetail(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bname = request.POST.get('book_name')
            aname = request.POST.get('author_name')
            quan = request.POST.get('quantity')
            email = request.user.email

            data = {
                'id' : id,
                'user':email,
                'book_name':bname,
                'author_name':aname,
                'quantity':quan,
            }

            headers = {'Content-type': 'application/json'}
            json_data = json.dumps(data)

            r = requests.put(f'http://127.0.0.1:8000/api/crud/{id}/', data=json_data, headers=headers)

            msg = r.json()

            print('-----------',r.status_code,msg)

            r = requests.get(f'http://127.0.0.1:8000/api/crud/{id}', params=request.GET)
            data = r.json()

            book_name = data['book_name']
            author_name = data['author_name']
            quantity = data['quantity']

            if (r.status_code == 200):
                mesg = 'Data updated successfully !!!'
            else:
                mesg = 'Something went wrong !!!' 

            return render(request, 'app/updateBookDetails.html', {'book_name':book_name, 'author_name':author_name,'quantity':quantity,'mesg':mesg})
        else:
            r = requests.get(f'http://127.0.0.1:8000/api/crud/{id}', params=request.GET)
            data = r.json()

            book_name = data['book_name']
            author_name = data['author_name']
            quantity = data['quantity']

            return render(request, 'app/updateBookDetails.html', {'book_name':book_name, 'author_name':author_name,'quantity':quantity})
    else:
        return HttpResponseRedirect('/login/')

@login_required
def deleteBook(request):
    email = request.user.email
    headers = {'Content-type': 'application/json'}
  
    r = requests.get(f'http://127.0.0.1:8000/bookinfo/{email}/', headers=headers)

    data = r.json()
    return render(request, 'app/deleteBook.html', {'data':data})

@login_required
def deleteBookDetail(request, id):
    data = {'id' : id}

    json_data = json.dumps(data)

    headers = {'content-Type':'application/json'}

    r = requests.delete(f'http://127.0.0.1:8000/api/crud/{id}/',headers=headers)     # put for update

    return HttpResponseRedirect('/deleteBook/')