from django.contrib import admin
from django.utils.html import format_html
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista de posts
    list_display = (
        'title',
        'author',
        'status',
        'published_date',
        'updated_date',
        'display_featured_image',
        'content_preview'
    )

    # Filtros laterales
    list_filter = ('status', 'published_date', 'author')

    # Campos de búsqueda
    search_fields = ('title', 'content', 'author__username')

    # Prepopulate slug from title
    prepopulated_fields = {'slug': ('title',)}

    # Campos editables directamente en la lista
    list_editable = ('status',)

    # Paginación
    list_per_page = 20

    # Orden por defecto
    ordering = ('-published_date',)

    # Campos en el formulario de edición
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'slug', 'author', 'status')
        }),
        ('Contenido', {
            'fields': ('content', 'featured_image')
        }),
        ('Fechas', {
            'fields': ('published_date',),
            'classes': ('collapse',)
        }),
    )

    # Métodos personalizados para list_display
    def display_featured_image(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.featured_image.url)
        return "-"
    display_featured_image.short_description = 'Imagen'

    def content_preview(self, obj):
        return format_html('<span title="{}">{}...</span>', obj.content, obj.content[:50])
    content_preview.short_description = 'Vista previa'

    # Personalización del formulario de creación
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Cuando se edita un objeto existente
            return ('created_date', 'updated_date')
        return ()
