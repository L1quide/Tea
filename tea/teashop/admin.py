from django.contrib import admin
from .models import Teapack, Category, Brand, Color, Tags, RaitingStar, Raiting, Picture, Reviews

@admin.register(Teapack)
class TeapackAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'cost', 'odlcost', 'sale', 'draft')
    list_filter = ('title', 'cost')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass

@admin.register(RaitingStar)
class RaitingStarAdmin(admin.ModelAdmin):
    pass

@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    list_display = ('ip', 'star')


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')



@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

