
from django.contrib import admin
from .models import Selection

#class CommentInline(admin.TabularInline):
    #model = Comment


#class ClientAdmin(admin.ModelAdmin):
    #inlines = [
        #CommentInline,
    #]



admin.site.register(Selection)
#admin.site.register(Comment)