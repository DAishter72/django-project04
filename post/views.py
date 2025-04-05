from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from post.models import Post


SUCCESS = '/posts/'


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # Specify your own template name/location
    context_object_name = 'posts'  # Default is 'object_list'
    ordering = ['-published_date']  # Order by published date descending


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'content', 'featured_image', 'status']
    # Usar reverse_lazy es mejor práctica
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


class PostEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'content', 'featured_image', 'status']
    success_url = SUCCESS  # Redirect to the list of posts after editing


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = SUCCESS  # Redirect to the list of posts after deletion
