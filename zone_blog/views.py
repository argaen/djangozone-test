from django.views.generic import DetailView
from django.views.generic.dates import ArchiveIndexView

from taggit.models import Tag

from models import Post, Project


class PostListView(ArchiveIndexView):
    context_object_name = 'objects'
    template_name = 'content_list.html'
    queryset = Post.objects.filter(is_published=True)
    paginate_by = 4
    date_field = 'published_on'

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        if "tag" in self.kwargs:
            queryset = queryset.filter(tags__name__in=[self.kwargs["tag"]])

        if "year" in self.kwargs and "month" in self.kwargs:
            queryset = queryset.filter(published_on__year=self.kwargs["year"], published_on__month=self.kwargs["month"])

        return queryset


class PostDetailView(DetailView):

    context_object_name = 'o'
    slug_field = 'slug'
    template_name = 'content_detail.html'
    queryset = Post.objects.filter(is_published=True)


class ProjectListView(ArchiveIndexView):
    context_object_name = 'objects'
    template_name = 'project_list.html'
    queryset = Project.objects.filter(is_published=True)
    date_field = 'published_on'

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['categories'] = Tag.objects.filter(project__is_published=True)
        return context


class ProjectDetailView(DetailView):

    context_object_name = 'o'
    slug_field = 'slug'
    template_name = 'project_detail.html'
    queryset = Project.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['objects'] = Project.objects.filter(is_published=True).exclude(pk=self.get_object().pk)
        return context
