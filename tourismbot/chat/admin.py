from django.contrib import admin
from . import models

# Register your models here.
class chatusermodel(admin.ModelAdmin):
    list_display = ['id', 'facebook_id', 'facebook_image']

    class Meta:
        model = models.chatusers

class destinationmodel(admin.ModelAdmin):
    list_display = ['id', 'name', 'longitude', 'latitude',
                    'defaultimage', 'owner', 'description', 'website',
                    'imageUrls', 'address', 'contact_number',
                    'image_one','image_two','image_three',
                    'image_four','image_five']
    class Meta:
        model = models.destinations

class servicesmodel(admin.ModelAdmin):
    list_display = ['id', 'destinations_fk', 'list_services']

    class Meta:
            model = models.services

class conversationsmodel(admin.ModelAdmin):
    list_display = ['id','facebook_fk','converse','timestamp']

    class Meta:
        model = models.conversations

class useraccountmodels(admin.ModelAdmin):
    list_display = ['id', 'username', 'password',
                    'email_address', 'facebook_connected_id',
                    'age', 'image']

    class Meta:
        model = models.user_accounts

admin.site.register(models.chatusers, chatusermodel)
admin.site.register(models.conversations, conversationsmodel)
admin.site.register(models.destinations, destinationmodel)
admin.site.register(models.services, servicesmodel)
admin.site.register(models.user_accounts, useraccountmodels)