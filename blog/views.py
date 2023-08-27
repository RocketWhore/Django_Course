from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from blog.models import Blog
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class MaterialsCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'body', 'preview', 'date_of_create', 'sign_of_pub', 'count_view')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
        return super().form_valid(form)


class MaterialsUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'body', 'preview', 'date_of_create', 'sign_of_pub', 'count_view')

    # success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class MaterialsListView(ListView):
    model = Blog
    succes_url = reverse_lazy('blog:list')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_of_pub=True)
        return queryset


class MaterialsDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.count_view += 1
        self.object.save()
        return self.object


class MaterialsDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
