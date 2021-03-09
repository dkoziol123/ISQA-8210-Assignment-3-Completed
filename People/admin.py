
from django.contrib import admin
from .models import People

#class CommentInline(admin.TabularInline):
    #model = Comment


#class ClientAdmin(admin.ModelAdmin):
    #inlines = [
        #CommentInline,
    #]



admin.site.register(People)
#admin.site.register(Comment)
