from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    category_pref1 = models.CharField(max_length=100, blank=True)
    category_pref2 = models.CharField(max_length=100, blank=True)
    category_pref3 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

# for saving news

class Articles(models.Model):
    author = models.CharField(max_length=1000, blank=True, default='Author', null=True)
    title = models.CharField(max_length=2500, blank=True, null=True)
    description = models.CharField(max_length=3000, blank=True, null=True)
    url = models.URLField(max_length=400, blank=True, null=True)
    url_to_image = models.URLField(max_length=500, blank=True, null=True)
    published_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
    # content = models.CharField(max_length=200,blank=True)


class Contact(models.Model):
    user_from = models.ForeignKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user_from} follow {self.user_to}'


# Adding following fields to User Dynamically
user_model = get_user_model()
user_model.add_to_class('following', models.ManyToManyField('self',
                                                            through=Contact,
                                                            related_name='followers',
                                                            symmetrical=False))


# Rating System
class Rating(models.Model):
    news = models.ForeignKey(Articles, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.FloatField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class News(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)

