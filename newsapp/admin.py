from django.contrib import admin
<<<<<<< HEAD
from .models import Profile
=======
from .models import Profile, Rating, Articles, Contact


>>>>>>> 7a59026 (Final Sprint)
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['user','date_of_birth','photo']
=======
    list_display = ['user', 'date_of_birth', 'photo']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'news', 'rating', 'status', 'created_at', 'updated_at']


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'description', 'url', 'url_to_image', 'published_at']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user_from','user_to','created']
>>>>>>> 7a59026 (Final Sprint)
