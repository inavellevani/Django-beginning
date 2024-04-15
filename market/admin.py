from django.contrib import admin
from django import forms
from market.models import Book, Author, Category


class BookForm(forms.ModelForm):
    author_name = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        widget=forms.TextInput(attrs={'placeholder': 'Enter author name'}),
        to_field_name='name'
    )
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple(verbose_name='Categories', is_stacked=False),
        to_field_name='name'
    )

    class Meta:
        model = Book
        fields = '__all__'

    def clean_author_name(self):
        name = self.cleaned_data['author_name']
        author, created = Author.objects.get_or_create(name=name)
        return author

    def clean_category(self):
        names = self.cleaned_data['category']
        categories = []
        for name in names:
            category, created = Category.objects.get_or_create(name=name)
            categories.append(category)
        return categories


class BooksAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('name', 'author_name', 'price', 'cover_type')
    search_fields = ('name', 'author_name')
    filter_horizontal = ('category',)


admin.site.register(Book, BooksAdmin)
