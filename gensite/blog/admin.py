from django.contrib import admin
from.models import aboutus
from.models import contactus
from.models import services

# Register your models here.
admin.site.register(aboutus)
admin.site.register(services)
#admin.site.register(contactus)


@admin.register(contactus)

class contactusAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'email','date_created']
