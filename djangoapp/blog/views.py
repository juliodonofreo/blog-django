from blog.models import Category, Page, Post, Tag
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

POSTS_PER_PAGE = 9


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "blog/pages/index.html"
    context_object_name = "posts"
    ordering = ("-created_at")
    queryset = Post.objects.get_published()
    paginate_by = POSTS_PER_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Home - "
        return context


class CreatedByListView(PostListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._temp_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_id = self.kwargs.get("author_id")
        print(f"\n{author_id}")
        user = self._temp_context["user"]

        user_name = user.username
        context.update({
            "page_title": f'posts de {user_name} - '
        })

        return context

    def get_queryset(self):
        qs = super().get_queryset()
        author_id = self._temp_context["author_id"]
        qs = qs.filter(created_by__pk=author_id)
        return qs

    def get(self, request, *args, **kwargs):
        author_id = self.kwargs.get("author_id")
        user = User.objects.filter(pk=author_id).first()

        if user is None:
            raise Http404()

        self._temp_context.update(
            {
                "author_id": author_id,
                "user": user
                }
        )

        return super().get(request, *args, **kwargs)


class CategoryListView(PostListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs.get("category").name
        context.update(
            {"page_title": f"{category_name} - "}
        )
        return context

    def get(self, request, *args, **kwargs):
        category_object = Category.objects\
            .filter(slug=self.kwargs.get("slug")).first()

        if not category_object:
            raise Http404

        self.kwargs.update({"category": category_object})
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset()\
            .filter(category__slug=self.kwargs.get("slug"))


def page(request, slug):
    page_obj = get_object_or_404(Page, slug=slug)
    if page_obj.is_published or request.user.is_staff:
        page_title = page_obj.title
        context = {"page": page_obj, 'page_title': f'{page_title} - '}
        return render(request, "blog/pages/page.html", context)
    raise Http404


def post(request, slug):
    post_obj = get_object_or_404(Post, slug=slug)

    if post_obj.is_published or request.user.is_staff:
        page_title = post_obj.title
        context = {"post": post_obj, 'page_title': f'{page_title} - '}
        return render(request, "blog/pages/post.html", context)
    raise Http404


def tag(request, slug):
    posts = Post.objects.get_published() \
        .filter(tag__slug=slug)
    tag_name = get_object_or_404(Tag, slug=slug).name

    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': f'{tag_name} - '
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
            'page_title': f'{search_value} - Search - ',
            "search_value": search_value
        }
    )
