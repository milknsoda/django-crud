from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def index(request):
    articles = Article.objects.order_by('-id')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    text = request.GET.get('text')
    article = Article.objects.create(title=title, content=text)
    # context = {
    #     'article': article
    # }
    # return render(request, 'articles/create.html', context)
    return redirect('articles:detail', article.pk)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    tmp = article.title
    article.delete()
    context = {
        'delete_tmp': tmp
    }
    return render(request, 'articles/delete.html', context)

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def edit_result(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.GET.get('title') != article.title or request.GET.get('text') != article.content:
        article.title = request.GET.get('title')
        article.content = request.GET.get('text')
        article.save()
    return redirect('articles:detail', article.pk)
