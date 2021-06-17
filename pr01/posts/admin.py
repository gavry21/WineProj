from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Author
from .models import Comment

class PostInstanceInLine(admin.StackedInline):
    model = Comment
    extra = 2

class PostModeAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'timestamp', 'updated', 'genre')
    list_display_links = ('title', 'content', 'timestamp', 'updated', 'genre')
    list_filter = ['timestamp']
    inlines = [PostInstanceInLine]
    #fields = ('title', 'content')
    exclude = ('timestamp', 'updated')
    ordering = ['-timestamp']
    
    class Meta:
        model = Post

class AuthorModeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name')
    ordering = ['second_name', 'first_name']
    class Meta:
        model = Author

class CommentModeAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_artical', 'comment_text')
    class Meta:
        model = Comment

admin.site.register(Post,PostModeAdmin)
admin.site.register(Author,AuthorModeAdmin)
admin.site.register(Comment, CommentModeAdmin)
