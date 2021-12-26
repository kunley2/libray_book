from django.shortcuts import render,redirect
from .form import BookForm
from .models import Novels

# Create your views here.

def index(request):
    book_list = Novels.objects.all()
    context = {'books':book_list}
    return render(request,'Books/index.html',context)


def register(request):

    if request.method == 'POST':
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {'form': form}
    form = BookForm()
    context = {'form': form}
    return render(request,'Books/create.html',context)

def detail(request,pk):
    book = Novels.objects.get(id=pk)
    context = {'book': book}
    if request.method == 'POST':
        book.delete()
        return redirect('index')
    return render(request,'Books/detail.html',context)