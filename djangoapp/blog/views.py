from blog.models import Category, Page, Post, Tag
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

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
    allow_empty = False

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

        self.kwargs.update({"category": category_object})
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset()\
            .filter(category__slug=self.kwargs.get("slug"))


class TagListView(PostListView):
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_name = self.kwargs.get("tag").name
        context.update(
            {"page_title": f"{tag_name} - "}
        )
        return context

    def get(self, request, *args, **kwargs):
        tag_object = Tag.objects\
            .filter(slug=self.kwargs.get("slug")).first()

        self.kwargs.update({"tag": tag_object})
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset()\
            .filter(tag__slug=self.kwargs.get("slug"))


class SearchListView(PostListView):
    def setup(self, request, *args, **kwargs) -> None:
        self._search_value = request.GET["search"].strip()
        return super().setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_value = self._search_value
        context.update(
            {
                "page_title": f"{search_value} - ",
                "search_value": search_value
                }
        )
        return context

    def get_queryset(self):
        search_value = self._search_value
        return super().get_queryset().filter(
            Q(title__icontains=search_value) |
            Q(excerpt__icontains=search_value) |
            Q(content__icontains=search_value)
        )

    def get(self, request, *args, **kwargs):
        if self._search_value == "":
            return redirect("blog:index")

        return super().get(request, *args, **kwargs)


class PageDetailView(DetailView):
    model = Page
    template_name = "blog/pages/page.html"
    slug_field = "slug"
    context_object_name = "page"
    NOT_FOUND_ERR_MSG = "Não possivel encontrar a página, \
tente novamente mais tarde"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_title = context["page"].title
        context.update({
            "page_title": f"{page_title} - "
        })
        return context

    def get_object(self, queryset=None):
        try:
            obj = super().get_object(queryset)
        except Http404:
            # Sobrescrevendo mensagem de erro pela customizada da classe.
            raise Http404(self.NOT_FOUND_ERR_MSG)
        return obj

    def get(self, request, *args, **kwargs):
        page_obj = self.get_object()
        if not (page_obj.is_published or request.user.is_staff):
            raise Http404(self.NOT_FOUND_ERR_MSG)
        return super().get(request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/pages/post.html"
    context_object_name = "post"
    NOT_FOUND_ERR_MSG = "Não possivel encontrar o post, \
tente novamente mais tarde"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_title = context["post"].title
        context.update({
            "page_title": f"{page_title} - "
        })
        return context

    def get_object(self, queryset=None):
        try:
            obj = super().get_object(queryset)
        except Http404:
            # Sobrescrevendo mensagem de erro pela customizada da classe.
            raise Http404(self.NOT_FOUND_ERR_MSG)
        return obj

    def get(self, request, *args, **kwargs):
        page_obj = self.get_object()
        if not (page_obj.is_published or request.user.is_staff):
            raise Http404(self.NOT_FOUND_ERR_MSG)
        return super().get(request, *args, **kwargs)
