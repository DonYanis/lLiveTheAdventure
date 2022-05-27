from django.contrib import admin

from .models import FeedBack, Notification, User,Trip,TripType,Blog,TripImage,Profile
# Register your models here.
admin.site.register(User)
admin.site.register(TripType)
admin.site.register(Trip)
admin.site.register(Blog)
admin.site.register(TripImage)
admin.site.register(Notification)
admin.site.register(FeedBack)
admin.site.register(Profile)
