from django.contrib import admin

# Register your models here.
from .models import Wine
from .models import Label
from .models import Sort
from .models import Comment

class WineInstanceInLine(admin.StackedInline):
    model = Comment
    extra = 2

class WineModeAdmin(admin.ModelAdmin):
    list_display = ('country', 'timestamp', 'updated')
    list_display_links = ('country', 'timestamp', 'updated')
    list_filter = ['timestamp']
    inlines = [WineInstanceInLine]
    #fields = ('title', 'content')
    exclude = ('timestamp', 'updated')
    ordering = ['-timestamp']
    
    class Meta:
        model = Wine

class LabelModeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year')
    ordering = ['name', 'year']
    class Meta:
        model = Label

class SortModeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ['name']
    class Meta:
        model = Sort       

class CommentModeAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_artical', 'comment_text')
    class Meta:
        model = Comment

admin.site.register(Wine,WineModeAdmin)
admin.site.register(Label,LabelModeAdmin)
admin.site.register(Sort,SortModeAdmin)
admin.site.register(Comment, CommentModeAdmin)
