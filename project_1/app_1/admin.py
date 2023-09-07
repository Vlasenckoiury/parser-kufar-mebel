from django.contrib import admin
from .models import Mebel


class MebelAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'description', 'parse_datetime']  # заголовки
    list_display_links = ['id', 'description']  # переход в карточку
    search_fields = ['id', 'price', 'description', 'parse_datetime']  # добавляет поиск([] по каким параметрам искать)
    # list_editable = ['price'] # позволяет в админке менять цену, не заходя в карточку
    list_filter = ['parse_datetime', 'price']


admin.site.register(Mebel, MebelAdmin)
