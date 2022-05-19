from django.contrib import admin

from listings.models import Band


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')  # fields we want to display in the band list of Django admin user
    # interface


admin.site.register(Band, BandAdmin)
