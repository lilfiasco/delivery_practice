from django.contrib import admin
from main import models


class FranchiseAdmin(admin.ModelAdmin):
    """FranchiseAdmin."""

    model = models.Franchise
    readonly_fields = ()
    list_display = [
        'title',
        'address',
    ]
    ordering = ('-id',)


# class RestaurantAdmin(admin.ModelAdmin):
#     """RestaurantAdmin."""

#     model = models.Restaurant

#     readonly_fields = ()
#     # list_filter = (
#     #     'title',
#     # )
#     list_display = (
#         'franchise',
#         'title',
#         'address',
#         'menu',
#     )
#     ordering = ('-id',)


class CategoryAdmin(admin.ModelAdmin):
    """CategoryAdmin."""

    model = models.Category

    readonly_fields = ()
    list_display = (
        'title',
    )
    ordering = ('-id',)


class FoodAdmin(admin.ModelAdmin):
    """FoodAdmin."""

    model = models.Food

    readonly_fields = ()
    list_display = (
        'title',
        'category',
        'description',
        'price',
        'image',
        'franchise',
    )
    ordering = ('-id',)


admin.site.register(models.Franchise, FranchiseAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Food, FoodAdmin)
