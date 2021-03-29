from django.shortcuts import render, redirect, HttpResponse
from .models import Article, Author

def articles(request):
    articles = Article.objects.all()
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


def add_article(request):
    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        date = request.POST["date"]
        article = Article(title=title, text=text , date=date)
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
    return HttpResponse("Успешно удалено!")