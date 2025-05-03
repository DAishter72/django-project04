from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from post.models import Post


@method_decorator(never_cache, name='dispatch')
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # Specify your own template name/location
    context_object_name = 'posts'  # Default is 'object_list'
    ordering = ['-published_date']  # Order by published date descending


@method_decorator(never_cache, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'content', 'featured_image', 'status']
    # Usar reverse_lazy es mejor práctica
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        # Establecer el autor
        form.instance.author = self.request.user

        # Generar slug automáticamente si no existe
        if not form.instance.slug:
            form.instance.slug = slugify(form.instance.title)

            # Asegurar que el slug sea único
            original_slug = form.instance.slug
            counter = 1
            while Post.objects.filter(slug=form.instance.slug).exists():
                form.instance.slug = f"{original_slug}-{counter}"
                counter += 1

        return super().form_valid(form)


@method_decorator(never_cache, name='dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'  # Usar slug en lugar de ID para las
    slug_url_kwarg = 'slug'


@method_decorator(never_cache, name='dispatch')
class PostEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'content', 'featured_image', 'status']
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    # Redirect to the list of posts after editing
    success_url = reverse_lazy('post_list')


@method_decorator(never_cache, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    # Redirect to the list of posts after deletion
    success_url = reverse_lazy('post_list')
