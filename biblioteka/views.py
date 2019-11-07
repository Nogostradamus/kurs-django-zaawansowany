from django.shortcuts import render
from django.http import HttpResponse
# from .signals import nasz_sygnal
from .models import Autor
from django.db import IntegrityError, transaction
from .models import Ksiazka

def glowna(request):
    # nasz_sygnal.send(sender=Autor, imie="Krystian")
    autor_id = 1
    jakias_funkcja(autor_id)
    return HttpResponse("To jest nasza glowna strona")



#@transaction.atomic
def jakias_funkcja(autor_id):

    autor = Autor.objects.get(id=autor_id)
    ostatnia = Ksiazka.objects.create(tytul="nowy", rok_wydania=2019, autor=autor)

    # try:
    #     with transaction.atomic():
    #         generate_relationships()
    # except IntegrityError:
    #     handle_exception()
    #
    # add_children()