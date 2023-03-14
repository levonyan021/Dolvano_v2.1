from django.contrib import admin
from .models import Rubric, Information, Color, ClockColor, Product


# Register your models here.


@admin.register(Product)
class WallClockAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_code', 'rubric', 'popular')
    search_fields = ('product_code', 'name')


class RubricAdmin(admin.ModelAdmin):
    pass


admin.site.register(Rubric, RubricAdmin)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('image1', 'description1')


@admin.register(ClockColor)
class ClockColorAdmin(admin.ModelAdmin):
    list_display = ('clock', 'color')
