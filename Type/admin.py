
from django.contrib import admin
from .models import Type

#class CommentInline(admin.TabularInline):
    #model = Comment


#class ClientAdmin(admin.ModelAdmin):
    #inlines = [
        #CommentInline,
    #]



admin.site.register(Type)
#admin.site.register(Comment)
