from django.contrib import admin
from .models import Character, Director, Movie, Product, Personal_Info, Feedback

admin.site.register(Character)
admin.site.register(Director)
admin.site.register(Movie)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    search_fields = ('person__email', 'person__name', 'person__surname')
    list_filter = ('like', 'characters', 'fav_producer')
@admin.register(Personal_Info)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone', 'contact', 'date')
    search_fields = ('email', 'name', 'surname')
