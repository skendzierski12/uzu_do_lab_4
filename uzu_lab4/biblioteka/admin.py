from django.contrib import admin


from .models import Genre, Author, Book, Osoba, Stanowisko

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)

"""Przygotuj i wykonaj migrację. Dodaj modele do panelu administracyjnego i zapisz do bazy po 3 instancje obiektu Stanowisko i Osoba"""

admin.site.register(Osoba)
admin.site.register(Stanowisko)
