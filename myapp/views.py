from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from myapp.forms import Book1Form, AuthorForm
from myapp.models import Book1


# Create your views here.

def register_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exists')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'This email already taken')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,first_name=first_name,
                                              last_name=last_name,email=email,
                                              password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password does not match')
            return redirect('register')

    return render(request,'user/register.html')
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('userlist')
        else:
            messages.info(request,"please provide correct credentials")
            return redirect('login')


    return render(request,'user/login.html')



def logout(request):
    auth.logout(request)
    return redirect('login')


def createbook(request):
    book = Book1.objects.all()

    if request.method == 'POST':
        form = Book1Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('booklist')

    else:
        form = Book1Form()

    return render(request, 'admin/book.html', {'form': form, 'books': book})


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('booklist')

    else:
        form = AuthorForm()
    return render(request, 'admin/author.html', {'form': form})


def listBook(request):
    books = Book1.objects.all()

    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)

    except EmptyPage:
        page = paginator.get_page(page_number.num_page)

    return render(request, 'admin/listBook.html', {'books': books, 'page': page})


def detailsBook(request, book_id):
    book = Book1.objects.get(id=book_id)
    return render(request, 'admin/details.html', {'book': book})


def updateBook(request, book_id):
    book = Book1.objects.get(id=book_id)

    if request.method == 'POST':
        form = Book1Form(request.POST, files=request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form = Book1Form(instance=book)

    return render(request, 'admin/update.html', {'form': form})


def deleteBook(request, book_id):
    book = Book1.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()

        return redirect('booklist')

    return render(request, 'admin/delete.html', {'book': book})


def index(request):
    return render(request, 'admin/base.html')


def searchbook(request):
    query = None
    books = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        books = Book1.objects.filter(Q(title__icontains=query))

    else:
        books = []

    context = {'books': books, 'query': query}
    return render(request, 'admin/search.html', context)

