from blog.models import Page, Post
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, render

POSTS_PER_PAGE = 9


# Create your views here.
def index(request):
    posts = Post.objects.get_published()
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def created_by(request, author_id):
    posts = Post.objects.get_published() \
        .filter(created_by__pk=author_id)
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def category(request, slug):
    posts = Post.objects.get_published() \
        .filter(category__slug=slug)
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def page(request, slug):
    page_object = get_object_or_404(Page, slug=slug)
    if page_object.is_published or request.user.is_staff:
        context = {"page": page_object}
        return render(request, "blog/pages/page.html", context)
    raise Http404


def post(request, slug):
    post_object = get_object_or_404(Post, slug=slug)
    if post_object.is_published or request.user.is_staff:
        context = {"post": post_object}
        return render(request, "blog/pages/post.html", context)
    raise Http404


def tag(request, slug):
    posts = Post.objects.get_published() \
        .filter(tag__slug=slug)
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def search(request):
    search_value = request.GET.get("search", "").strip()

    posts = Post.objects.get_published() \
        .filter(
            Q(title__icontains=search_value) |
            Q(excerpt__icontains=search_value) |
            Q(content__icontains=search_value)
        )
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )
