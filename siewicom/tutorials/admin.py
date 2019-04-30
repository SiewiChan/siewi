from django.contrib import admin
from .models import Category,Tutorials,Articles


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category')

class TutorialsAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','category','image')

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','article','author')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Tutorials,TutorialsAdmin)
admin.site.register(Articles,ArticlesAdmin)
