from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Youtuber(models.Model):
    camera_choices = (
        ('canon', 'canon',),
        ('nikon', 'nikon',),
        ('sony', 'sony',),
        ('red', 'red',),
        ('fuji', 'fuji',),
        ('panasonic', 'panasonic',),
        ('other', 'other',),
    )

    category_choices = (
        ('code', 'code',),
        ('mobile_reviews', 'mobile_reviews',),
        ('vlogs', 'vlogs',),
        ('comedy', 'comedy',),
        ('gaming', 'gaming',),
        ('film_making', 'film_making',),
        ('cooking', 'cooking',),
    )

    crew_choices = (
        ('solo', 'solo',),
        ('small', 'small',),
        ('large', 'large',),
    )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/ytubers/%Y/%m')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField(default=20)
    height = models.IntegerField()
    crew = models.CharField(max_length=255, choices=crew_choices)
    camera_type = models.CharField(max_length=255, choices=camera_choices)
    subs_count = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=category_choices)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name