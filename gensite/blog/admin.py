from django.contrib import admin
from.models import aboutus
from.models import contactus
from.models import services
from.models import clientdata
from.models import  Dynamicslider
from.models import  Portfolio
from.models import  Gallery
from.models import  Team

# Register your models here.
admin.site.register(aboutus)
admin.site.register(services)
admin.site.register(clientdata)
admin.site.register(Dynamicslider)
admin.site.register(Portfolio)
admin.site.register(Gallery)
admin.site.register(Team)

# admin.site.register(contactus)


@admin.register(contactus)

class contactusAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'email','date_created']
    search_fields = ('name',)
    list_filter =('date_created',)
    list_per_page = 10
    # list_editable =('date_created',)
