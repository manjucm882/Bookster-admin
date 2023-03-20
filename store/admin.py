from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import *


class BookForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=FilteredSelectMultiple("Categories", False),
        required=False,
    )

    class Meta:
        model = Book
        fields = "__all__"


class BookAdmin(admin.ModelAdmin):
    form = BookForm


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(language_written)
admin.site.register(Writer)
admin.site.register(Review)
admin.site.register(Slider)