from django.http import HttpResponse
from django.shortcuts import render_to_response 
from mysite.books.models import Author
from mysite.books.models import Book
import datetime
correct_flag = False
author_flag = False
flag1 = False
flag2 = False
flag3 = False
flag4 = False
def search(request):
    errors = []
    authors = Author.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('You input nothing.')
        else:
            author = Author.objects.filter(Name=q)
            books = Book.objects.filter(AuthorID = author)
            return render_to_response('search_results.html',{'query':q,'books':books,'author':author})
    return render_to_response('search_form.html',{'errors':errors,'authors':authors})

def search_again(request,offset):
    dbook = Book.objects.get(Title=offset)
    author = dbook.AuthorID
    q = author.Name
    dbook.delete()
    books = Book.objects.filter(AuthorID = author)
    return render_to_response('search_results.html',{'query':q,'books':books})
                
        
def detail(request,offset):
    book = Book.objects.get(Title=offset)
    author = book.AuthorID
    return render_to_response('detail.html',{'book':book,'author':author})

def search_add(request):
    global flag1
    global flag2
    global flag4
    global author_flag
    flag1 = False
    flag2 = False
    flag4 = False
    author_flag = False
    if request.POST:
        post = request.POST
        try:
            author = Author.objects.get(AuthorID=post["AuthorID"])
            if 'save_author' in post:
                author_flag = True
                return render_to_response('search_add_author.html',{'author_flag':author_flag})
        except:
            if 'save_book' in post:
                return render_to_response('search_add_author.html')
            elif 'save_author' in post:
                post = request.POST
                if post["AuthorID"]=='' or post["Name"]=='' or post["Age"]=='' or post["Country"]=='' :
                    flag4 = True
                    return render_to_response('search_add_author.html',{'blank_flag':flag4})
                else:
                    author =Author(
                        AuthorID = post["AuthorID"],
                        Name = post["Name"],
                        Age = post["Age"],
                        Country = post["Country"])
                author.save()
                return render_to_response('search_add_book.html')
        author = Author.objects.get(AuthorID=post["AuthorID"])
        if post["ISBN"]=='' or post["Title"]=='' or post["Publisher"]=='' or post["PublishDate"]=='' or  post["Price"]=='' :
            flag2 = True
            return  render_to_response('search_add_book.html',{'blank_flag':flag2})
        else:
            new_book = Book(
                ISBN = post["ISBN"],
                Title = post["Title"],
                AuthorID = author,        
                Publisher = post["Publisher"],
                PublishDate= post["PublishDate"],
                Price = post["Price"])          
            new_book.save()
            flag1 = True
    return render_to_response('search_add_book.html',{'flag':flag1})


def update(request,offset):
    global flag3
    global correct_flag
    global author_flag
    new_book = Book.objects.get(Title=offset)
    correct_flag = False
    author_flag = False
    flag3 = False
    flag2 = False
    if request.POST:
        post = request.POST
        try:
            author = Author.objects.get(AuthorID=post["AuthorID"])
            if 'save_author' in post:
                author_flag = True
                return render_to_response('search_add_author.html',{'author_flag':author_flag})
        except:
            if 'save_update' in post:
                return render_to_response('search_add_author.html')
            elif 'save_author' in post:
                post = request.POST
                if post["AuthorID"]=='' or post["Name"]=='' or post["Age"]=='' or post["Country"]=='':
                    flag3 = True
                    return render_to_response('search_add_author.html',{'blank_flag':flag3})
                else:
                    author = Author(
                        AuthorID = post["AuthorID"],
                        Name = post["Name"],
                        Age = post["Age"],
                        Country = post["Country"])
                    author.save()
                    return render_to_response('update.html',{'books':new_book})
        if post["Publisher"]=='' or post["PublishDate"]=='' or post["Price"]=='' :
             flag2 = True
             return  render_to_response('search_add_book.html',{'blank_flag':flag2})
        Book.objects.filter(Title=offset).update(
            AuthorID = Author.objects.get(AuthorID=post["AuthorID"]),
            Publisher = post["Publisher"],
            PublishDate= post["PublishDate"],
            Price = post["Price"])
        correct_flag = True
    return render_to_response('update.html',{'books':new_book,'correct_flag':correct_flag})
        
    