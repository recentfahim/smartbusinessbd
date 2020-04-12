from django.contrib import admin
from .models import Contact, User, TempData, Subscription, Payment

admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Payment)
admin.site.register(Subscription)
admin.site.register(TempData)
