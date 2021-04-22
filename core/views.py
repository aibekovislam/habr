from django.shortcuts import render, redirect, HttpResponse
from .models import Article, Author
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required


User = get_user_model()


def articles(request):
    articles = Article.objects.all()
    articles = Article.objects.order_by('-date')
    return render(
        request,
        "articles.html",
        {"articles": articles}
    )

def authors(request):
    authors = Author.objects.all()
    return render(
        request,
        "authors.html",
        {"authors": authors}
    )

def article_page(request, id):
    article = Article.objects.get(id=id)
    article.views += 1
    article.save()
    return render(
        request,
        "article_page.html",
        {"article": article}
    )


def about(request):
    return render(request, "about.html")


def homepage(request):
    return render(request, "index.html")


def edit_article(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.text = request.POST.get("text")
        article.save()
        return redirect(article_page, pk)
    return render(request, "update.html", {"article": article})

@login_required(login_url = '/login/')
def add_article(request):
    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        picture = request.FILES.get('picture')
        article = Article(title=title, text=text, picture=picture)
        user = request.user
        if not Author.objects.filter(user=user).exists():
            author = Author(user=user, nik=user.username)
            author.save()
        author = user.author
        article.author = author
        article.save()
        return redirect(articles)
    return render(request, "add_news.html")


def delete_article(request, id):
    article = Article.objects.get(pk=id)
    article.delete()
    return redirect(articles)



def search(request):
    word = request.GET.get("word")
    articles = Article.objects.filter(
        Q(title__icontains=word) | Q(text__icontains=word),
        is_active=True)
    return render(request, "articles.html", {"articles": articles})


def author(request, pk):
    author = Author.objects.get(pk=pk)
    return render(
        request,
        "author_page.html",
        {"author": author}
    )


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('articles')
    return render(request, "login.html")


def sign_out(request):
    logout(request)
    return redirect(sign_in)


def reg(request):
    if request.method == 'GET':
        return render(request, "register.html")
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(
            username=username,
            password=password
            )
        return redirect(sign_in)




def acc(request):
    return render(request, "account.html")
    