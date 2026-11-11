from django.shortcuts import render, redirect
from myapp.my_forms import BookForm
from myapp.models import Book

# Create your views here.
def home(request):
    books = Book.objects.all()#selects everything from Books
    return render(request, 'home.html',{'books':books})

def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        #Validating input
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add.html',{'form':form})