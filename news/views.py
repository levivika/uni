from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import News, Category



def index(request):
    news_list = News.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'news_list': news_list,
        'categories': categories,
    }
    return render(request, 'news/index.html', context)


@login_required
def profile(request):
    user_news = News.objects.filter(author=request.user)
    categories = Category.objects.all()
    context = {
        'user_news': user_news,
        'categories': categories,
    }
    return render(request, 'news/profile.html', context)


@login_required
def add_news(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        category = Category.objects.filter(id=category_id).first() if category_id else None
        image = request.FILES.get('image')

        News.objects.create(
            title=title,
            description=description,
            category=category,
            author=request.user,
            image=image
        )
        return redirect('profile')

    return render(request, 'news/add_news.html', {'categories': categories})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('index')

    return render(request, 'news/register.html')


def logout_user(request):
    logout(request)
    return redirect('index')


def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'news/news_detail.html', {'news': news_item})


def category_news(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    news_list = News.objects.filter(category=category).order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'news_list': news_list,
        'categories': categories,
        'selected_category': category
    }
    return render(request, 'news/index.html', context)


@login_required
def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id, author=request.user)
    categories = Category.objects.all()

    if request.method == 'POST':
        news.title = request.POST.get('title')
        news.description = request.POST.get('description')
        category_id = request.POST.get('category')
        news.category = Category.objects.filter(id=category_id).first() if category_id else None

        if 'image' in request.FILES:
            news.image = request.FILES['image']

        news.save()
        return redirect('news_detail', news_id=news.id)

    context = {
        'news': news,
        'categories': categories
    }
    return render(request, 'news/edit_news.html', context)



@login_required
def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id, author=request.user)

    if request.method == 'POST':
        news.delete()
        return redirect('profile')

    return render(request, 'news/delete_confirm.html', {'news': news})
