from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from IPython import embed

from .models import Article, Comment

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-id')
    context = {
        'articles': articles
    }
    # embed()
    return render(request, 'articles/index.html', context)

# def new(request):
#     # if request.method == 'GET':
#     return render(request, 'articles/new.html')
#     # else: # 'POST'
#     #     title = request.POST.get('title')
#     #     content = request.POST.get('content')
#     #     article = Article(title=title, content=content)
#     #     article.save()
#     #     return redirect('articles:detail', article.pk)

def create(request):
    # 저장 로직
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(title=title, content=content)
        article.save()
        return redirect('articles:detail', article.pk)
    # context = {
    #     'article': article
    # }
    # return render(request, 'articles/create.html', context)
    # embed()
    else:
        return render(request, 'articles/new.html')

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment = article.comment_set.all()
    context = {
        'article': article,
        'comments': comment
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')
    # tmp = article.title
    # article.delete()
    # context = {
    #     'delete_tmp': tmp
    # }
    # return render(request, 'articles/delete.html', context)

# def edit(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     context = {
#         'article': article
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('text')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {
            'article': article
        }
        return render(request, 'articles/edit.html', context)

@require_POST
def comment_create(request, article_pk):
    content = request.POST.get('comment')
    comment = Comment.objects.create(content=content, article_id=article_pk)
    messages.info(request, '댓글이 등록되었습니다.')
    return redirect('articles:detail', article_pk)

@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    messages.success(request, '댓글이 삭제되었습니다.')
    return redirect('articles:detail', article_pk)