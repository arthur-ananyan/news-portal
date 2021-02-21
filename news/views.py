from news.models import Category, News
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):

    page = request.GET.get('page', 1)
    news_list = News.objects.all().order_by('-creation_date')
    paginator = Paginator(news_list, 10)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {
        'categories': Category.objects.all(),
        'news': news
    })


def category_list(request):

    page = request.GET.get('page', 1)
    news_list = News.objects.all().order_by('-creation_date')
    paginator = Paginator(news_list, 10)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {
        'categories': Category.objects.all(),
        'news': news
    })


def category_selected(request, category_name):

    page = request.GET.get('page', 1)
    news_list = News.objects.filter(
        category__name=category_name).order_by('-creation_date')
    paginator = Paginator(news_list, 10)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'category_selected.html', {

        'news': news,
        'selected_category': Category.objects.get(name=category_name),
        'categories': Category.objects.exclude(name=category_name),
    })


def news_details(request, pk):

    return render(request, 'details.html', {
        'categories': News.objects.get(id=pk).category.select_related(),
        'news': News.objects.get(id=pk),
    })
