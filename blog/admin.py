from django.contrib import admin
from .models import Post ,Category ,Comment
#from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    emty_value_display = '-empty-'
    list_display = ('title','author','status','created_date','id')
    list_filter = ('published_date',)
    search_fields = ('title','content','author')
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    emty_value_display = '-empty-'
    list_display = ('name','post','approved','created_date')
    list_filter = ('published_date',)
    search_fields = ('post','name','approved')

admin.site.register(Comment ,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
