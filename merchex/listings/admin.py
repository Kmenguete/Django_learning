from django.contrib import admin

from listings.models import Band

from listings.models import Title


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')  # fields we want to display in the band list of Django admin user
    # interface


class TitleAdmin(admin.ModelAdmin):
    list_display = ('title', )  # fields we want to display in the title list of Django admin user interface


admin.site.register(Band, BandAdmin)

admin.site.register(Title, TitleAdmin)
